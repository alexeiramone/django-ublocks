
function encodeURIforLinkto(value) {
  return encodeURI(value.toString().toLowerCase()
    .replace(/^\s+|\s+$/g, '')      // Trim
    .replace(/\s+/g, '-')           // Replace spaces with -
    .replace(/\-\-+/g, '-')         // Replace multiple - with single -
    )
}

function CustomFileBrowser(field_name, url, type, win) {
    
    var cmsURL = '/admin/filebrowser/browse/?pop=2';
    cmsURL = cmsURL + '&type=' + type;
    
    tinyMCE.activeEditor.windowManager.open({
        file: cmsURL,
        width: 980,  // Your dimensions may differ - toy around with them!
        height: 500,
        resizable: 'yes',
        scrollbars: 'yes',
        inline: 'no',  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: 'no'
    }, {
        window: win,
        input: field_name,
        editor_id: tinyMCE.selectedInstance.editorId
    });
    return false;
}

tinyMCE.init({
    
    // see http://www.tinymce.com/wiki.php/Configuration
    
    // Init
    mode: 'specific_textareas',
    editor_deselector: 'mceNoEditor',
    theme: 'advanced',
    skin: 'default',
    
    // Templates
    // external_template_list_url: "/static/tinymce_template_list.js",
    // template_external_list_url: "/static/tinymce_template_list.js",
    // media_external_list_url: "/static/tinymce_template_list.js",

    // General
    entity_encoding: 'raw',
    // entity_encoding: 'named', // vai trocar todos acentos por entities
    verify_html: true,
    accessibility_warnings: false,
    browsers: 'gecko,msie,safari,opera',
    keep_styles: false,
    object_resizing: true,
    plugins: 'save,advimage,advlink,paste,media,searchreplace,template,contextmenu,table,inlinepopups,visualchars',
    tools: 'inserttable',
    // directionality : "rtl",
    dialog_type: 'modal', // inlinepopups
    
    // Callbacks
    file_browser_callback: 'CustomFileBrowser',
    
    // Cleanup/Output
    element_format: 'html',
    fix_list_elements: true,
    forced_root_block: 'p',
    // style formsts overrides theme_advanced_styles
    // see http://www.tinymce.com/wiki.php/Configuration:style_formats
    style_formats: [
        {title: 'Marked Text', inline : 'mark'},
        {title: 'Keyboard', inline : 'kbd'}
    ],
    verify_html: true,

    // URL
    relative_urls: false,
    document_base_url : "/",
    remove_script_host: true,

    // Layout
    width: 800,
    height: 400,
    indentation: '10px',
    
    // Content CSS
    // customize your content ...
    content_css : "/static/tinymce_content.min.css",
    
    schema: "html5",

    // Theme Advanced
    theme_advanced_toolbar_location: 'top',
    theme_advanced_toolbar_align: 'left',
    theme_advanced_statusbar_location: 'bottom',
    theme_advanced_buttons1: 'save,|,formatselect,styleselect,|,bold,italic,underline,|,bullist,numlist,blockquote,sub,sup,|,undo,redo,|,hr,justifyleft,justifycenter,justifyright,justifyfull,|,indent,outdent,|,link,unlink,|,image,charmap,visualchars',
    theme_advanced_buttons2: 'search,|,cut,copy,paste,pasteword,|,media,|,table,tablecontrols,|,removeformat,cleanup,code',
    theme_advanced_path: false,
    theme_advanced_blockformats: 'p,h2,h3,h4,pre,code',
    theme_advanced_resizing: true,
    theme_advanced_resize_horizontal: false,
    theme_advanced_resizing_use_cookie: true,
    
    // Removi galeria_placeholder
    // Save Django Pra ficar na mesma página!

    save_onsavecallback: function() {
        document.getElementsByName('_continue')[0].click()
    },

    // Image Plugin
    // see http://www.tinymce.com/wiki.php/Plugin:advimage
    theme_advanced_styles: 'Image Left=img_left;Image Right=img_right;Image Block=img_block',
    advimage_update_dimensions_onchange: true,
    
    table_styles: 'Table=table;Stripped=table table-striped;Bordered=table table-bordered;Condensed=table table-condensed',
    table_row_styles: 'Success=success;Error=error;Warning=warning;Info=info',
    //table_cell_styles: '',

    // Link Settings
    // see http://www.tinymce.com/wiki.php/Plugin:advlink
    advlink_styles: 'Internal Link=internal;External Link=external',

    // Media Plugin
    // see http://www.tinymce.com/wiki.php/Plugin:media
    media_strict: true,
    
    // Grappelli Settings
    grappelli_adv_hidden: false,
    grappelli_show_documentstructure: 'on',


    setup : function(ed) {

        ed.addButton('image_caption_left', {
            title : 'Bloco Imagem e legenda pra esquerda',
            image : '/static/img/tinymce_image_left.png',
            onclick : function() {
                ed.focus();
                texto = ed.selection.getContent();
                ed.selection.setContent('<div class="img_left metade"><img src="https://placeholdit.imgix.net/~text?txtsize=20&bg=ffcc00&txtclr=000000&txt=Usar%20Varia%C3%A7%C3%A3o%20%22Livre%20Metade%22%20ou%20%22Chamada%20Metade%22&w=383&h=215&txttrack=0" alt="[Colocar Alt]" class="img-responsive"><p class="figcaption">Legenda ' + texto + '</p></div>');
            }
        });

        ed.addButton('image_caption_right', {
            title : 'Bloco Imagem e legenda pra direita',
            image : '/static/img/tinymce_image_right.png',
            onclick : function() {
                ed.focus();
                texto = ed.selection.getContent();
                ed.selection.setContent('<div class="img_right metade"><img src="https://placeholdit.imgix.net/~text?txtsize=20&bg=ffcc00&txtclr=000000&txt=Usar%20Varia%C3%A7%C3%A3o%20%22Livre%20Metade%22%20ou%20%22Chamada%20Metade%22&w=383&h=215&txttrack=0" alt="[Colocar Alt]" class="img-responsive"><p class="figcaption">Legenda ' + texto + '</p></div>');
            }
        });

        ed.addButton('galeria_placeholder', {
            title : 'Posicionador de Galeria',
            image : '/static/img/tinymce-galeria-placeholder.png',
            onclick : function() {
                ed.focus();
                ed.selection.setContent('<p>[GALERIA]</p>');
            }
        });

        ed.addButton('columns_4x4', {
            title : 'Duas colunas (50%/50%)',
            image : '/static/img/tinymce_columns_4x4.png',
            onclick : function() {
                ed.focus();
                ed.selection.setContent('<div class="row"><div class="col-sm-6">1</div><div class="col-sm-6">2</div></div>');
            }
        });

        ed.addButton('columns_2x2x2x2', {
            title : 'Três colunas (33%/33%/33%)',
            image : '/static/img/tinymce_columns_2x2x2x2.png',
            onclick : function() {
                ed.focus();
                ed.selection.setContent('<div class="row"><div class="col-sm-4">1</div><div class="col-sm-4">2</div><div class="col-sm-4">3</div></div>');
            }
        });

        ed.addButton('columns_6x2', {
            title : 'Duas colunas (66%/33%)',
            image : '/static/img/tinymce_columns_6x2.png',
            onclick : function() {
                ed.focus();
                ed.selection.setContent('<div class="row"><div class="col-sm-8">1</div><div class="col-sm-4">2</div></div>');
            }
        });

        ed.addButton('columns_2x6', {
            title : 'Duas colunas (33%/66%)',
            image : '/static/img/tinymce_columns_2x6.png',
            onclick : function() {
                ed.focus();
                ed.selection.setContent('<div class="row"><div class="col-sm-4">1</div><div class="col-sm-8">2</div></div>');
            }
        });

    }
    
    // Elements
    // valid_elements: '@[id|class|style|title|dir<ltr?rtl|lang|xml::lang|onclick|ondblclick|'
    // + 'onmousedown|onmouseup|onmouseover|onmousemove|onmouseout|onkeypress|'
    // + 'onkeydown|onkeyup],a[rel|rev|charset|hreflang|tabindex|accesskey|type|'
    // + 'name|href|target|title|class|onfocus|onblur],strong/b,em/i,strike,u,'
    // + '#p,-ol[type|compact],-ul[type|compact],-li,br,img[longdesc|usemap|'
    // + 'src|border|alt=|title|hspace|vspace|width|height|align],-sub,-sup,'
    // + '-blockquote,-table[border=0|cellspacing|cellpadding|width|frame|rules|'
    // + 'height|align|summary|bgcolor|background|bordercolor],-tr[rowspan|width|'
    // + 'height|align|valign|bgcolor|background|bordercolor],tbody,thead,tfoot,'
    // + '#td[colspan|rowspan|width|height|align|valign|bgcolor|background|bordercolor'
    // + '|scope],#th[colspan|rowspan|width|height|align|valign|scope],caption,-div,'
    // + '-span,-code,-pre,address,-h1,-h2,-h3,-h4,-h5,-h6,hr[size|noshade],-font[face'
    // + '|size|color],dd,dl,dt,cite,abbr,acronym,del[datetime|cite],ins[datetime|cite],'
    // + 'object[classid|width|height|codebase|*],param[name|value|_value],embed[type|width'
    // + '|height|src|*],script[src|type],map[name],area[shape|coords|href|alt|target],bdo,'
    // + 'button,col[align|char|charoff|span|valign|width],colgroup[align|char|charoff|span|'
    // + 'valign|width],dfn,fieldset,form[action|accept|accept-charset|enctype|method],'
    // + 'input[accept|alt|checked|disabled|maxlength|name|readonly|size|src|type|value],'
    // + 'kbd,label[for],legend,noscript,optgroup[label|disabled],option[disabled|label|selected|value],'
    // + 'q[cite],samp,select[disabled|multiple|name|size],small,'
    // + 'textarea[cols|rows|disabled|name|readonly],tt,var,big',
    // extended_valid_elements : 'embed[width|height|name|flashvars|src|bgcolor|align|play|'
    // + 'loop|quality|allowscriptaccess|type|pluginspage]'
    
});


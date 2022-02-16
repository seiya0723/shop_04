//ページが読み込みされた時に function(){} の中の処理を実行する。
window.addEventListener("load" , function (){

    //$から始まるものはjQuery構文、予めjQueryをインストールしておかないと使えない
    //class名add_imageに対して、クリックした時、idがimage_areaの中にinputタグを追加する
    //$(".add_image").on("click",function(){ $("#image_area").append('<input type="file" name="image">'); });
    //$(".input_image").on("input",function(){ $("#image_area").append('<input class="imput_image" type="file" name="image">'); })

    $(document).on("input", ".input_image" ,function(){ $("#image_area").append('<input class="input_image" type="file" name="image">'); })

    //$("#submit").on("click" ,function() { send(); });

});

/*
function send(){

    console.log("Ajax送信");

    let form_elem   = "#form_area";
    //FormDataのオブジェクトを作る
    let data        = new FormData( $(form_elem).get(0) );
    //#form_areaのaction属性の値を調べる
    let url         = $(form_elem).prop("action");
    let method      = $(form_elem).prop("method");
    
    $.ajax({
        url: url,
        type: method,
        data: data,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr ) { 
        console.log("ここでページの部分的なレンダリング処理を行う。")
    }).fail( function(xhr, status, error) {
        console.log("通信エラー、サーバー側のエラー")
    }); 
}
*/


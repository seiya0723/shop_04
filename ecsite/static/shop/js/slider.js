window.addEventListener("load" , function (){

    //クリックした時、scroll()を実行する。押された要素(this)とブーリアン値(NextとPrevを見分ける)を引数にする。
    $(".previous_button").on("click",function(){ scroll(this,false); });
    $(".next_button").on("click",    function(){ scroll(this,true); });

});
//scroll関数
function scroll(elem,next){

    /* クリックされた箇所のスクロールする要素を抜き取る */
    let target  = $(elem).siblings(".data_preview_area");

    let all_width       = target.get(0).scrollWidth;
    let single_width    = target.outerWidth();
    let position_width  = target.scrollLeft();

    var   test_var = "これは関数内で使える変数です";
    let   test_let = "ブロック内で使える変数です。varと違って変数の再宣言ができない。同じ変数名塗りつぶされないようにする時";
    const test_const = "これは定数です。書き換えと再宣言はできません。"

    //先頭、末端までスクロールしたら、それぞれ戻る、進むができないように(jQueryアニメーション遅延問題)

    //positionのleft,rightに対して位置を指定した場合、1ページの移動を指定すると、例えば残り2個の場合、2個だけ表示される。
    //スクロールの場合、1ページ移動を指定したとして、はみ出た値を指定することになっても、残り2個が末端に表示される
    if ( (next) && ( all_width > single_width + position_width ) ){
        target.animate({ scrollLeft:"+=" + String(single_width) } , 300);
    }
    else if ( (!next) && ( 0 < position_width ) ){
        //前に戻る、かつ 1ページ目以降を表示している場合のみ戻る
        target.animate({ scrollLeft:"-=" + String(single_width) } , 300);
    }
}


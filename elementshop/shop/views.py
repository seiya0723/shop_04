from django.shortcuts import render,redirect
from django.views import View

from .models import Product,Cart
from .forms import CartForm


class IndexView(View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["products"] = Product.objects.all()

        return render(request, "shop/index.html", context)

index   = IndexView.as_view()


class ProductView(View):

    def get(self, request, pk, *args, **kwargs):
        #TODO:ここで商品の個別ページを表示
        return redirect("shop:index")

    def post(self, request, pk, *args, **kwargs):
        #ここでユーザーのカートへ追加
        if request.user.is_authenticated:

            copied  = request.POST.copy()

            copied["user"]      = request.user.id
            copied["product"]   = pk

            form    = CartForm(copied)

            if form.is_valid():
                print("バリデーションOK")

                #TIPS:ここで既に同じ商品がカートに入っている場合、レコード新規作成ではなく、既存レコードにamount分だけ追加する。
                cart    = Cart.objects.filter(user=request.user.id, product=pk).first()

                if cart:
                    #受けとった数量を数値に変換させる
                    cleaned = form.clean()

                    #元の数値の属性値に追加加算。
                    cart.amount += cleaned["amount"]

                    #保存する。これでカートの中の同じ商品の数量が加算される。
                    cart.save()

                else:          
                    #存在しない場合は新規作成
                    form.save()

            else:
                print("バリデーションNG")

        else:
            print("未認証です")
            #TODO:未認証ユーザーにはCookieにカートのデータを格納するのも良い

        return redirect("shop:index")

product = ProductView.as_view()


class CartView(View):

    def get(self, request, *args, **kwargs):
        #ここでカートの中身を表示

        context             = {}

        if request.user.is_authenticated:
            context["carts"]    = Cart.objects.filter(user=request.user.id)
        else:
            #TODO:未認証ユーザーにはCookie格納されたカートのデータを表示するのも良い
            pass

        return render(request, "shop/cart.html", context)

cart = CartView.as_view()



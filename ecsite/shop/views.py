from django.shortcuts import render,redirect
from django.views import View


from .models import Product,ProductCategory,ProductImage
from .forms import ProductForm,ProductImageForm

class IndexView(View):
    
    def get(self, request, *args, **kwargs):

        context                 = {}
        context["products"]     = Product.objects.all()
        context["categories"]   = ProductCategory.objects.all()

        return render(request,"shop/index.html",context)

    def post(self, request, *args, **kwargs):

        #出品処理
        form    = ProductForm(request.POST)

        if not form.is_valid():
            print("バリデーションエラー")
            print(form.errors)
            return redirect("shop:index")
            
        product     = form.save()

        #ここで保存したデータのIDを取得する、AjaxはそのIDを受取、画像をセットして再度リクエストを送る。
        product_id  = product.id
        
        return redirect("shop:index")


index   = IndexView.as_view()




# game-inventory
Tugas 3 PBP

Tautan aplikasi: https://growtopia-shop.adaptable.app/

1. UserCreationForm adalah form yang disediakan oleh Django untuk mempermudah dalam mengimplementasikan sebuah formulir pendaftaran sebuah akun user pada 
   website kita. Form ini by default sudah menyediakan field pendaftaran akun user baru pada umumnya seperti field username dan password. Tidak hanya itu, 
   field yang disediakan juga sudah diatur dengan validasi bawaan yang mengatur pengisian username dan passwordnya.

   Kelebihan:
   + Mudah digunakan, karena ini merupakan form bawaan yang sudah siap pakai yang disediakan oleh Django
   + Fleksibilitas cukup tinggi, karena kita dapat mengatur komponen-komponen yang ada pada form ini

   Kekurangan:
   + Perlu autentikasi lanjutan, form ini hanya berguna untuk membuat sebuah user baru dan perlu menambahkan fitur lainnya seperti login, logout, dsb
   + Tidak mudah dicustomize, form ini cukup sulit jika ingin kita modifikasi secara lanjut
  
2. + **AUTENTIKASI**
     Autentikasi adalah proses verifikasi pengguna (user) yang mencoba mengakses sebuah laman/aplikasi. Tujuan dari autentikasi ini adalah untuk mengecek 
     apakah pengguna yang mencoba mengakses sudah terdaftar atau tidak. Biasanya autentikasi melibatkan pengecekan username, password, dsb. <br><br>
   + **AUTORISASI**
     Autorisasi adalah proses mengatur hak akses pengguna yang telah melewati tahap autentikasi. Tujuan dari adanya autorisasi adalah untuk membatasi hak akses user yang sudah login ke website atau aplikasi kita.

3. Cookies adalah data yang berisikan informasi pengguna yang dapat diakses oleh  website. Cookies itu sendiri memiliki batas waktu tertentu dan akan secara otomotasi setelah batas waktu tercapai. Django mengambil menyediakan metode bawaan untuk mengatur dan mengambil cookies.


4. Penggunaan cookies dalam suatu website pada umumnya aman. Namun, perlu diperhatikan bahwa masih ada risiko yang dapat mengancam keamanan data pada cookies, seperti kebocoran data, penyalahgunaan data dari cookies, dan hal lainnya. Hal ini dapat diatasi dengan mengenkripsi data cookies dengan baik  

5. + Menambahkan fungsi register, login, dan logout pada file views.py 
     1. Register

     ```python
      from django.shortcuts import redirect
      from django.contrib.auth.forms import UserCreationForm
      from django.contrib import messages  


      def register(request):
         form = UserCreationForm()

         if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  form.save()
                  messages.success(request, 'Your account has been successfully created!')
                  return redirect('main:login')
         context = {'form':form}
         return render(request, 'register.html', context)
     ```

     2. Login dan logout

     ```python
        from django.contrib.auth import authenticate, login
        from django.contrib.auth import logout

        def login_user(request):
            if request.method == 'POST':
               username = request.POST.get('username')
               password = request.POST.get('password')
               user = authenticate(request, username=username, password=password)
               if user is not None:
                     login(request, user)
                     return redirect('main:show_main')
             else:
                     messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            context = {}
            return render(request, 'login.html', context)    

         def logout_user(request):
            logout(request)
            return redirect('main:login')
     ```

   + Membuat file login.html dan register.html pada direktori main/templates
   + Menambahkan path baru dari file html yang telah dibuat
     
     ```python
        from main.views import login_user
        from main.views import logout_user

        ...
        path('register/', register, name='register'), 
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        ...
     ```

   + Membuat dua akun user dengan melakukan register pada app, lalu menambahkan   tiga data yang berbeda dengan cara menambahkan item baru
   + Menghubungkan item dengan user
     
     1. Menambahkan potongan kode pada file models.py
        ```python
            ...
            from django.contrib.auth.models import User
            ...
            class Product(models.Model):
               user = models.ForeignKey(User, on_delete=models.CASCADE)
               ...
        ```

     2. Mengubah function create_product dan show_main pada views.py
        ```python
           ...
           def show_main(request):
               products = Product.objects.filter(user=request.user)

               context = {
                  'name': request.user.username,
               ...

           def create_product(request):
               form = ProductForm(request.POST or None)

               if form.is_valid() and request.method == "POST":
                  product = form.save(commit=False)
                  product.user = request.user
                  product.save()
                  return HttpResponseRedirect(reverse('main:show_main'))
            ...
        ```

   

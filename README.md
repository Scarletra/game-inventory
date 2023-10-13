# game-inventory
Tugas 6 PBP

Name: Fernando Valentino Sitinjak
Class: PBP F
Student ID: 2206081332

Tautan aplikasi: https://growtopia-shop.adaptable.app/

1. **Synchronus programming** adalah pemrograman yang mana sebuah tugas dapat dijalankan saat tugas-tugas sebelumnya sudah selesai dikerjakan. Singkatnya, untuk menjalankan suatu tugas, harus menunggu tugas lain terlebih dahulu dikerjakan

   **Asynchronus programming** adalah pemrograman yang mana dalam satu waktu komputer dapat menjalankan beberapa operasi, sehingga tidak akan memakan waktu yang lama dibandingkan dengan synchronus programming

2. **Event-driven programming** terjadi ketika komputer mengeksekusi sebuah program yang ditentukan oleh suatu peristiwa(event). Dalam konteks tugas ini, salah satu contoh event-driven programming adalah ketika kita menekan tombol untuk menampilkan sebuah form yang akan nantinya akan menambahkan data baru ke web kita.

3. Penerapan asynchronus programming pada AJAX salah satunya adalah saat kita membuat HTTP request yang biasanya menggunakan method GET atau POST. Pada saat request ini dijalankan, program JavaScript tidak akan terhenti meskipun sedang menunggu respon dari server

4. **Fetch API** merupakan built-in JavaScript yang menggunakan promise-based, sehingga dapat mengatasi request secara asinkron. Fetch API sangatlah fleksibel karena dapat digunakan dalam berbagai HTTP request.

   **JQuery** merupakan teknologi yang mudah untuk dipelajari dan digunakan. Sama seperti Fetch API, JQuery juga mampu menangani request secara asinkron.


5. + **AJAX GET** 
      Menambahkan script pada file main.html. Fungsi dari async funct tersebut adalah untuk mengambil data secara asinkron dan menampilkannya dengan model Card
      ```html
      async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
      }

      async function refreshProducts() {
         document.getElementById("product_table").innerHTML = ""
         const products = await getProducts()
         let htmlString = ''
         products.forEach((item) => {
               htmlString += `\n<div class="card bg-danger bg-gradient border border-white" style="width: 15rem;">
               <img src="https://th.bing.com/th/id/OIP.wYN6Vv4FwuPkt2u8YhvQFgHaFk?w=217&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7" class="card-img-top" alt="...">
                  <div class="card-body">
                     <h5 class="card-title">${item.fields.name}</h5>
                     <p class="card-text">Price: ${item.fields.price} || Amount: ${item.fields.amount}</p>
                     <p class="card-text">${item.fields.description}</p>
                     <a href="#"><button type="button" class="btn btn-dark">Edit</button></a>
                     <a href="#"><button type="button" class="btn btn-dark">Delete</button></a>
                     <p>${item.fields.date_added}</p>
                  </div>
               </div>` 
         })
         
         document.getElementById("product_table").innerHTML = htmlString
      }

      ```

   + **AJAX POST**
      Menambahkan kode untuk form dan button pada HTML dan juga menambahkan script
      ```html
         <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
         <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="form" onsubmit="return false;">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="name" class="col-form-label">Name:</label>
                            <input type="text" class="form-control" id="name" name="name"></input>
                        </div>
                        <div class="mb-3">
                            <label for="price" class="col-form-label">Price:</label>
                            <input type="number" class="form-control" id="price" name="price"></input>
                        </div>
                        <div class="mb-3">
                            <label for="amount" class="col-form-label">Amount:</label>
                            <input type="number" class="form-control" id="amount" name="amount"></input>
                        </div>
                        <div class="mb-3">
                            <label for="description" class="col-form-label">Description:</label>
                            <textarea class="form-control" id="description" name="description"></textarea>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                </div>
            </div>
        </div>
    </div>
   

      Menambahkan fungsi baru pada views.py
      ```python
         def add_product_ajax(request):
            if request.method == 'POST':
               name = request.POST.get("name")
               price = request.POST.get("price")
               amount = request.POST.get("amount")
               description = request.POST.get("description")
               user = request.user

               new_product = Item(name=name, price=price, amount=amount, description=description, user=user)
               new_product.save()

               return HttpResponse(b"CREATED", status=201)

            return HttpResponseNotFound()
      ```


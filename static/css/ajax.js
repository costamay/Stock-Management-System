<!-- <h1>
  great

</h1> -->
{%extends "base.html"%}
{% load bootstrap4 %}
{% load static %}
{% block content %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    

    <title>Document</title>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-light main" style="background-color: #ffffff;">
        <a class="navbar-brand" href="#"><strong>DASHBOARD</strong></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="navbar-collapse collapse w-100 order-3 dual-collapse2">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item" style="float:right">
                    <a class="nav-link" href="#"><i class="fas fa-bell"></i></a>
                </li>
                <li class="nav-item" style="float:right">
                    <a class="nav-link" href="#"><i class="fas fa-cog"></i></a>
                </li>
                <li class="nav-item" style="float:right">
                    <a class="nav-link" href="/logout/">Logout<i class="fas fa-bell"></i></a>
                </li>
            </ul>
        </div>
    </nav>

    <div id="mySidenav" class="sidenav">
        <!-- <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a> -->
        <p class="taste_afrique">TASTE AFRIQUE</p>
        <div style="text-align: center;">
            <i class="fas fa-user-circle fa-7x"></i>
            <p style="color: #ffffff;">{{ user }}</p>
        </div>
        <button class="dropdown-btn">Product
            <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-container">
           
            <a href="{% url 'add_product' %}">Add Product</a>
            <a href="">Manage Product</a>
        </div>

        <button class="dropdown-btn">Client
            <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-container">
            <a href="#">Add Client</a>
            <a href="#">Manage Client</a>
        </div>

        <button class="dropdown-btn">Supplier
            <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-container">
            <a href="{% url 'add_supplier' %}">Add Supplier</a>
            <a href="{% url 'all_suppliers' %}">Manage Supplier</a>
        </div>

        <button class="dropdown-btn">Order
            <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-container">
            <a href="#">Add Order</a>
            <a href="#">Manage Order</a>
        </div>

        <button class="dropdown-btn">Purchase
            <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-container">
            <a href="#">Add Purchase</a>
            <a href="#">Manage Purchase</a>
        </div>
    </div>

    <!-- <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; open</span> -->

    <div class="container" style="width: 750px;">
        <div class="col-md-12 mt-5">
            <div class="jumbotron">
                <h1 class="display-4">Product</h1>
                <hr class="my-4">
                <table class="table table-borderless">
                    <thead class="border-bottom font-weight-bold">
                        <tr>
                            <td>Product Name</td>
                            <td>Product Size</td>
                            <td>Product Quantity</td>
                            <td>Product Category</td>
                            <td>Product Image</td>
                            <td>Product Price</td>
                            <td>
                                <a href="{% url 'add_product' %}" class="btn btn-outline-success">
                                    <i class="fas fa-plus"></i> Add New
                                </a>
                            </td>
                        </tr>
                    </thead>
                    <tbody id="ajax">
                          
                    </tbody>
                </table>
            
            </div>
        </div>
    </div>

    <script>

        $(document).ready(function () {
            (function () {
                console.log(Math.PI);
            })();
            (function () {
                $.ajax({
                    type: "get",
                    url: "{% url 'product_list' %}",
                    contentType: 'application/json',
                    success: function (data) {
                         for (i=0;i<Object.keys(data).length ;i++){
                            console.log(data[i]);

                            $('#ajax').append(
                                "<tr>"+
                                    "<td>"+data[i].fields.product_name+"</td>"+
                                    "<td>"+data[i].fields.product_size+"</td>"+
                                    "<td>"+data[i].fields.product_qyt+"</td>"+
                                    "<td>"+data[i].fields.product_image+"</td>"+
                                    "<td>"+data[i].fields.product_category+"</td>"+
                                    "<td>"+data[i].fields.product_price+"</td>"+
                                    
                               "</tr>"+
                              " <td>"+
                                `<a href="//localhost:8000/products/${data[i].pk}" <i class='far fa-edit fa-lg'> </i> </a>`+
                               ` <form action="" method="post" class="d-inline">
                                    {% csrf_token %}
                                    <button type="submit" class="btn">
                                        <i class="far fa-trash-alt fa-lg text-danger float-right"></i>
                                    </button>
                                </form>`+
                            "</td>"

                            )
                        }
                       
                    },
                    error: function () {
                        alert("error");

                    }
                })
                })();
            })
            var dropdown = document.getElementsByClassName("dropdown-btn");
            var i;
    
            for (i = 0; i < dropdown.length; i++) {
                dropdown[i].addEventListener("click", function () {
                    this.classList.toggle("active");
                    var dropdownContent = this.nextElementSibling;
                    if (dropdownContent.style.display === "block") {
                        dropdownContent.style.display = "none";
                    } else {
                        dropdownContent.style.display = "block";
                    }
                });
            }     
        </script>


</body>

</html>

{% endblock %}
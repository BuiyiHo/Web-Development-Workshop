
var cart = {}

var table = document.querySelector("#table")
var str = table.innerHTML
for(let item of items){
    str+= "<tr> \
                <td>name: "+item.name+"</td> \
                <td>$: "+item.price+"</td> \
                <td><img src='"+item.url+"'/></td> \
                <td>&nbsp<lable>quantity</lable><input id='quantity"+item.name+"' type='number' value=1></td> \
                <td><button onclick=\"add('"+item.name+"')\">add</button></td> \
           </tr>"
}


table.innerHTML = str

function add(name) {
    console.log(name)
    var cart = document.querySelector("#cart")
    var str = ""
    var total = 0
    var j = []
    if(window.cart[name]){
        var q = document.querySelector("#quantity"+name).value
        window.cart[name]+=parseInt(q)
    }
    else{
        var q = document.querySelector("#quantity"+name).value
        window.cart[name]=parseInt(q)
        console.log(window.cart)
    }

    for(let i of items){
        if(window.cart[i.name]){
            var obj = {}
            str+="<div>"+i.name+" "+window.cart[i.name]+"</div>"
            total+=window.cart[i.name]*i.price
            obj['name'] = i.name
            obj['price'] = i.price
            obj['qty'] = window.cart[i.name]
            obj['total'] = window.cart[i.name]*i.price
            j.push(obj)
        }
    }
    cart.innerHTML = str
    var newitem = document.createElement("h2")
    newitem.innerText="TOTAL:$ "+total
    var newitem2 = document.createElement("input")
    newitem2.type="hidden"
    newitem2.name="list"
    newitem2.value=JSON.stringify(j)
    cart.appendChild(newitem)
    var form = document.querySelector("#form")
    form.appendChild(newitem2)

}
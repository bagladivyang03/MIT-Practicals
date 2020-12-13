function changeImage(){
    var x = document.getElementById('harryID');
    if(x.src.match('harry.PNG')) {
        x.src = 'images/harry1.PNG';
    } 
    else {
        x.src = 'images/harry.PNG';
    }
}


function changeText(){
    document.getElementById('textID').innerHTML = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and  scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.";
}


function changecolor(){
    document.getElementById('colorID').style.color = "white";
    document.getElementById('colorID').style.fontStyle = "normal";
}

function addnodetoParent(){
    var node = document.createElement("LI");
    var textnode = document.createTextNode("Nestlé Smarties Book Prizes (1997–1999)");
    node.appendChild(textnode);                              
    document.getElementById("awards").appendChild(node);     
}

function deletenodefromParent(){
    var l = document.getElementById('awards');
    l.removeChild(l.childNodes[0])
}

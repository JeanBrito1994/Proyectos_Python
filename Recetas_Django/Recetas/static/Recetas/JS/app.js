
function validar()
{
	var rut, nombre, apellido, correo, password, expresion, expre;

	nombre = document.getElementById("nombre").value; 
	rut = document.getElementById("rut").value; 
	apellido = document.getElementById("apellido").value; 
	correo = document.getElementById("correo").value; 
	password = document.getElementById("password").value; 
	expresion = /\w+@+\w+\.+[a-z]/;
	expre = /^[a-zA-Z\s]*$/;
	

	if(nombre === "" || rut === "" || apellido === "" || correo === "" || password === "")
	{
		alert("Debe llenar todos los campos");
		return false;
	}

	else if(nombre.length>20 || apellido.length>20 )
	{
		alert("El nombre o apellido es muy largo");
		return false;
		
	}
	else if(!expre.test(nombre))
	{
		alert("El nombre no corresponde al formato");
		return false;
	}
	else if(!expre.test(apellido))
	{
		alert("El apellido no corresponde al formato");
		return false;
	}
	
	else if(rut.length>9 || rut.length<8)
	{
		alert("El rut no es valido");
		return false;		
	}
	
	else if(correo.length>50)
	{
		alert("El correo es muy largo");
		return false;
	}
	else if(!expresion.test(correo))
	{
		alert("El correo no corresponde al formato");
		return false;
	}
	
	else if(isNaN(rut))
	{
		alert("El rut no corresponde al formato");
		return false;
	}

}
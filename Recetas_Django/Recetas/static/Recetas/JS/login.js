function validarlogin()
{
	var usuario, contraseña, expresion;

	usuario = document.getElementById("usuario").value; 
	contraseña = document.getElementById("contraseña").value; 
	expresion = /\w+@+\w+\.+[a-z]/;

	if(usuario === "" || contraseña === "")
	{
		alert("Debe llenar todos los campos");
		return false;
	}

	else if(!expresion.test(usuario))
	{
		alert("El usuario no corresponde al formato");
		return false;
	}

	else if(contraseña.length>9 || contraseña.length<8)
	{
		alert("El largo de la contraseña no es correcto");
		return false;		
	}
}
<html>
	<head> 
		<title> Registration Form </title>
	</head>
	<body>
		<h2> Register </h2>
		<form method="post" action="register.php">
			<label> Full Name </labe>
			<input type="text" name="fullname"> <br>
			<label> User Name </label>
			<input type="text" name="username"> <br>
			<label> Password </label>
			<input type="password" name="p1"> <br>
			<label> Re-enter Password </label>
			<input type="password" name="p2"> <br>
			<button type="submit" name="reg"> Register </button> <br>
			Already a registered user?
			<a href="login.php">Sign In </a>
		</form>
	</body>
</html>

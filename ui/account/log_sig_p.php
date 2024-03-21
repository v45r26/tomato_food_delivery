<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>TOMATO FOOD DELIVERY</title>

	<!-- Fav Icon -->
	<link rel="icon" type="image/x-icon" href="../assets/logo/main.png">

	<!-- Font Awesome -->
	<link rel="stylesheet" type="text/css" href="../assets/external_assets/fontawesome-free-5.13.1-web/css/all.min.css">

	<!-- CSS -->
	<link rel="stylesheet" type="text/css" href="../css/log_sig_p.css">

	<!-- EEL JS -->
	<script type="text/javascript" src="/eel.js"></script>

	
</head>
<body>


<div class="wrapper">
	<header>
		<span class="he_sp active_btn" id="log_d" onclick="dis_log_in_f()">LOGIN</span>
		<span class="he_sp" id="sign_d" onclick="dis_sign_up_f()">SIGNUP</span>
	</header>

	<div class="log_up_f" id="log_in_f">
		<form action="#" id="login_form">
			<div class="form_input">
				<input type="text" id="login_user_name" placeholder="Enter Username">
			</div>
			<div class="form_input">
				<input type="text" id="login_password" placeholder="Password">
			</div>
			<div class="form_input sub_btn">
				<button type="submit" id="log_in_sub_btn">Login</button>
			</div>
		</form>
	</div>

	<div class="log_up_f" id="sign_up_f" style="display: none;">
		<form action="#" id="signup_form">
			<div class="form_input">
				<input type="text" id="sgup_name" placeholder="Name">
			</div>
			<div class="form_input">
				<input type="text" id="sgup_user_name" placeholder="Username">
			</div>
			<div class="form_input">
				<input type="text" id="sgup_email" placeholder="Email">
			</div>
			<div class="form_input">
				<input type="text" id="sgup_password" placeholder="Password">
			</div>
			<div class="form_input">
				<input type="text" id="sgup_c_password" placeholder="Confirm Password">
			</div>
			<div class="form_input sub_btn">
				<button type="submit" name id="sign_up_sub_btn">Signup</button>
			</div>
		</form>
	</div>
</div>

<div class="errTxt" id="errTxt"></div>

<script type="text/javascript">
	const log_d = document.querySelector('span#log_d'),
		  sign_d = document.querySelector('span#sign_d'),
		  sign_up_f = document.querySelector('div#sign_up_f'),
		  log_in_f = document.querySelector('div#log_in_f'),
		  errTxt = document.querySelector('#errTxt');


	errTxt.style.display = 'none';

	function dis_sign_up_f() 
	{
		sign_d.classList.add('active_btn');
		log_d.classList.remove('active_btn');
		log_in_f.style.display = 'none';
		sign_up_f.style.display = '';
	}
	function dis_log_in_f() 
	{
		log_d.classList.add('active_btn');
		sign_d.classList.remove('active_btn');
		sign_up_f.style.display = 'none';
		log_in_f.style.display = '';
	}
// JS for Login
	const login_form = document.querySelector('#login_form'),
	 	  log_in_sub_btn = login_form.querySelector('#log_in_sub_btn'),
	 	  login_user_name = login_form.querySelector('#login_user_name'),
	 	  login_password = login_form.querySelector('#login_password');

	login_form.onsubmit = (e)=>
	{
		e.preventDefault();
	}

	log_in_sub_btn.onclick = ()=>
	{
		if (login_user_name.value == '') 
		{
			console.log('Please Fill all the Field!');
			errTxt.innerHTML = 'Please Fill all the Field!';
			errTxt.style.display = '';
		}
		else
		{
			if (login_password.value == '')
			{
				console.log('Please Fill all the Field!');
				errTxt.innerHTML = 'Please Fill all the Field!';
				errTxt.style.display = '';
			}
			else
			{
				console.log(login_user_name.value+' | '+login_password.value);
				var log_cred = login_user_name.value+'|'+login_password.value;
				eel.login(log_cred)(status);
				function status(cd)
				{
					if (cd == 'success') 
					{
						console.log(cd);
						// login_form.reset();
						window.location.href = '../tab/index.html?un='+login_user_name.value;
					}
					else
					{
						console.log(cd)
						errTxt.innerHTML = cd;
						errTxt.style.display = '';
					}
				}
			}
		}
	}

// JS for Signup
	const signup_form = document.querySelector('#signup_form'),
	 	  sign_up_sub_btn = signup_form.querySelector('#sign_up_sub_btn'),
	 	  sgup_name = signup_form.querySelector('#sgup_name'),
	 	  sgup_user_name = signup_form.querySelector('#sgup_user_name'),
	 	  sgup_email = signup_form.querySelector('#sgup_email'),
	 	  sgup_password = signup_form.querySelector('#sgup_password'),
	 	  sgup_c_password = signup_form.querySelector('#sgup_c_password');


	signup_form.onsubmit = (e)=>
	{
		e.preventDefault();
	}
	sign_up_sub_btn.onclick = ()=>
	{

		if(sgup_name.value == '')
		{
			console.log('Please Fill all the Field!');
			errTxt.innerHTML = 'Please Fill all the Field!';
			errTxt.style.display = '';
		}
		else if (sgup_user_name.value == '') 
		{
			console.log('Please Fill all the Field!');
			errTxt.innerHTML = 'Please Fill all the Field!';
			errTxt.style.display = '';
		}
		else if (sgup_email.value == '')
		{
			console.log('Please Fill all the Field!');
			errTxt.innerHTML = 'Please Fill all the Field!';
			errTxt.style.display = '';
		}
		else if (sgup_password.value == '')
		{
			console.log('Please Fill all the Field!');
			errTxt.innerHTML = 'Please Fill all the Field!';
			errTxt.style.display = '';
		}
		else if (sgup_c_password.value == '')
		{
			console.log('Please Fill all the Field!');
			errTxt.innerHTML = 'Please Fill all the Field!';
			errTxt.style.display = '';
		}
		else
		{
			console.log(sgup_name.value+'|'+sgup_user_name.value+'|'+sgup_email.value+'|'+sgup_password.value+'|'+sgup_c_password.value);
		
			if (sgup_password.value == sgup_c_password.value) 
			{
				var log_cred = sgup_name.value+'|'+sgup_user_name.value+'|'+sgup_email.value+'|'+sgup_password.value+'|'+sgup_c_password.value;
				eel.signup(log_cred)(status);
				function status(cd)
				{
					if (cd == 'success') 
					{
						console.log(cd);
						dis_log_in_f();
						signup_form.reset();
					}
					else
					{
						console.log('Error Occoured!');
						console.log(cd)
						errTxt.innerHTML = 'Error occoured!';
						errTxt.style.display = '';
					}
				}
			}
			else
			{
				console.log('Password not Matched!');
				errTxt.innerHTML = 'Password not Matched!';
				errTxt.style.display = '';
			}
		}
	}

</script>
</body>
</html>
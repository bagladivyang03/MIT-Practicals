        
        function validateform(){
            var fname = document.forms["signupform"]["firstname"];
            var lname = document.forms["signupform"]["lastname"];
            var emailval = document.forms["signupform"]["email"];
            var phoneno = document.forms["signupform"]["phoneNumber"];
            var password = document.forms["signupform"]["password"];
            var passwordconfirm = document.forms["signupform"]["passwordConfirmation"];
            if(fname.value.trim()==null || fname.value.trim()=="" || fname.value ===" "){
                alert("This field cant be Empty!. Please enter your First name");
                fname.focus();
                return false;
            }
            if(lname.value.trim()==null || lname.value.trim()=="" || lname.value === " " ){
                alert("This field cant be Empty!. Please enter your Last name");
                lname.focus();
                return false;
            }
            if(emailval.value.trim()==null || emailval.value.trim()=="" || emailval.value === " " ){
                alert("This field cant be Empty!. Please enter your Email ID");
                emailval.focus();
                return false;
            }
            var x=emailval.value;  
            var atposition=x.indexOf("@");  
            var dotposition=x.lastIndexOf(".");  
            if (atposition<1 || dotposition<atposition+2 || dotposition+2>=x.length){  
            alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);  
            return false;
            }
            if(phoneno.value.trim()==null || phoneno.value.trim()=="" || phoneno.value === " " ){
                alert("This field cant be Empty!. Please enter your Phone No");
                phoneno.focus();
                return false;
            }
            function checkphoneNo(phone){
                var regexp =/^\d{10}$/
                if(phone.match(regexp))
                {
                    return true;
                }
                else{
                    return false;
                }
            }
            if(!checkphoneNo(phoneno.value)){
                alert("Phone no not valid!");
                phoneno.focus();
                return false;
            }
            if( password.value == "" ){
                alert("This field cant be Empty!. Please enter your Password")
                password.focus();
                return false;
            }
            var paswd=  /^(?=.*[0-9])(?=.*[A-Z])(?=.*[!$#@&])[a-zA-Z0-9!$#@&]{7,}$/;
            if(!paswd.test(password.value)){
                alert("Password must contain one Captial Alphabet, one number, one special character and must be of atleast length 7");
                password.focus();
                return false;
            }
            if(passwordconfirm.value == "" ){
                alert("This field cant be Empty!. Please confirm your password")
                passwordconfirm.focus();
                return false;
            }
            if(password.value != passwordconfirm.value){
                alert("Password not matched !");
                passwordconfirm.foccus();
                return false;
            }
            alert("Form Validated Successfully!!")
            return true;
        }
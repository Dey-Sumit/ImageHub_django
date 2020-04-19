$(document)
  .ready(function() {
    $('.ui.form')
      .form({
        fields: {
          username: {
            identifier: 'username',
            rules: [
              {
                type   : 'empty',
                prompt : 'Please enter a username'
              }
            ]
          },
          password: {
            identifier  : 'password',
            rules: [
              {
                type   : 'empty',
                prompt : 'Please enter your password'
              }
            ]
          }
        }
      })
    ;
  })
;
$('.ui.dropdown')
  .dropdown()
;
$('.ui.checkbox').checkbox();

function openSignUp() {
    $('.ui.modal')
    .modal('setting', 'transition', 'scale')
    .modal({blurring: true})
    .modal('show');
}

$(document)
  .ready(function() {
    $('.ui.form')
      .form({
        fields: {
          fname: {
            identifier: 'fname',
            rules: [
              {
                type   : 'empty',
                prompt : 'Please enter your first name'
              }
            ]
          },
          email: {
            identifier  : 'email',
            rules: [
              {
                type   : 'empty',
                prompt : 'Please enter your e-mail'
              },
              {
                type   : 'email',
                prompt : 'Please enter a valid e-mail'
              }
            ]
          },
          gender: {
            identifier: 'gender',
            rules: [
              {
                type   : 'empty',
                prompt : 'Please select a gender'
              }
            ]
          },
          username: {
            identifier: 'username',
            rules: [
              {
                type   : 'empty',
                prompt : 'Please enter a username'
              }
            ]
          },
          password: {
            identifier: 'password',
            rules: [
              {
                type   : 'empty',
                prompt : 'Please enter a password'
              },
              {
                type   : 'minLength[6]',
                prompt : 'Your password must be at least 6 characters'
              }
            ]
          },
          mobile: {
            identifier: 'mobile',
            rules: [
              {
                type   : 'empty',
                prompt : 'Please enter a mobile number'
              },
              {
                type   : 'minLength[10]',
                prompt : 'Your mobile number should be of 10 characters'
              }
            ]
          },
        }
      })
    ;
});

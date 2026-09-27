
<!DOCTYPE HTML>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>JupyterHub</title>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
      <link rel="stylesheet"
            href="/hub/static/css/style.min.css?v=1169d53348a10b2020fa67f02516a65c955f1483603703fdb5d65653c099dc66f2a52246ae0856c6f1ebcc5e1c5f527a3fa9210d12e6d8ec77e0e095d9b2c734"
            type="text/css" />
    
    
      <link rel="icon" href="/hub/static/favicon.ico?v=fde5757cd3892b979919d3b1faa88a410f28829feb5ba22b6cf069f2c6c98675fceef90f932e49b510e74d65c681d5846b943e7f7cc1b41867422f0481085c1f" type="image/x-icon">
    
    
      <script src="/hub/static/components/bootstrap/dist/js/bootstrap.bundle.min.js?v=1ef3a326b7703690db9062481b664da83955a8ca3beea6ece0c7b871a8741e80eb7e1adb03ef12065667d4aaef010c3b7082cb3c526f770220a61cd098c9be3f"
              type="text/javascript"
              charset="utf-8"></script>
      <script src="/hub/static/components/requirejs/require.js?v=1ff44af658602d913b22fca97c78f98945f47e76dacf9800f32f35350f05e9acda6dc710b8501579076f3980de02f02c97f5994ce1a9864c21865a42262d79ec"
              type="text/javascript"
              charset="utf-8"></script>
      <script src="/hub/static/components/jquery/dist/jquery.min.js?v=bf6089ed4698cb8270a8b0c8ad9508ff886a7a842278e98064d5c1790ca3a36d5d69d9f047ef196882554fc104da2c88eb5395f1ee8cf0f3f6ff8869408350fe"
              type="text/javascript"
              charset="utf-8"></script>
      <script src="/hub/static/js/darkmode.js?v=2fd9a7d11ad78df9351fed40ab35eab52e1e6a3d516f188b652120e6faf57b8e387a30aae8f52a6fb51563d06d04545c7005da0b77a98c21b0bd28f6d1cdfa11"
              type="text/javascript"
              charset="utf-8"></script>
    
    
    
    <script type="text/javascript">
      require.config({
        
        urlArgs: "v=20260923221121",
        
        baseUrl: '/hub/static/js',
        paths: {
          components: '../components',
          jquery: '../components/jquery/dist/jquery.min',
          moment: "../components/moment/moment",
        },
      });

      window.jhdata = {
        base_url: "/hub/",
        prefix: "/",
        
        
        admin_access: false,
        
        
        options_form: false,
        
        xsrf_token: "MnwxOjB8MTA6MTc5MDQ3NDg2NXw1Ol94c3JmfDY4OlRtOXVaVHA1TVVGTmEyMVJkM0UzVlhsTmRqRm9SM1ZUZEZCcWJ6TTVjMlZLVlVkNFYxTjZaWGsyU0ZGWVJFWlpQUT09fDBmYTNmYWUyMTFmZTZhYWY0NWJhNjBkODAyNGFiZDdmMDc1OGEwYzZmNDUxOTE0NzVhMmVjYjNiMGYyODgyODY",
      };

</script>
    
    
      <meta name="description" content="JupyterHub">
      <meta name="keywords" content="Jupyter, JupyterHub">
    
  </head>
  <body>
    <noscript>
      <div id='noscript'>
        JupyterHub requires JavaScript.
        <br>
        Please enable it to proceed.
      </div>
    </noscript>
    
      <nav class="navbar navbar-expand-sm bg-body-tertiary mb-4">
        <div class="container-fluid">
          
            <span id="jupyterhub-logo" class="navbar-brand">
              <a href="/hub/">
                <img src='/hub/logo'
                     alt='JupyterHub logo'
                     class='jpy-logo'
                     title='Home' />
              </a>
            </span>
          
          
          <div class="collapse navbar-collapse" id="thenavbar">
            <ul class="navbar-nav me-auto mb-0">
              
            </ul>
            <ul class="nav navbar-nav me-2">
              
                <li class="nav-item">
                  
                    <button class="btn btn-sm"
                            id="dark-theme-toggle"
                            aria-label="Toggle dark mode"
                            title="Toggle dark mode">
                      <i aria-hidden="true" class="fa fa-circle-half-stroke"></i>
                    </button>
                  
                </li>
                <li class="nav-item">
                  

                </li>
              
            </ul>
          </div>
          
          
        </div>
      </nav>
    
    
      
    
    
  
    <div id="login-main" class="container">
      
        
          <form action="/hub/login?next=%2Fhub%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3Djupyterhub-user-g31257740%26redirect_uri%3D%252Fuser%252Fg31257740%252Foauth_callback%26response_type%3Dcode%26state%3DSbXb8PICx1E6EfyFgn54vQ" method="post" role="form">
            <div class="auth-form-header">
              <h1>Sign in</h1>
            </div>
            <div class='auth-form-body m-auto'>
              <p id='insecure-login-warning' class='hidden alert alert-warning'>
                Warning: JupyterHub seems to be served over an unsecured HTTP connection.
                We strongly recommend enabling HTTPS for JupyterHub.
              </p>
              
              <input type="hidden" name="_xsrf" value="MnwxOjB8MTA6MTc5MDQ3NDg2NXw1Ol94c3JmfDY4OlRtOXVaVHA1TVVGTmEyMVJkM0UzVlhsTmRqRm9SM1ZUZEZCcWJ6TTVjMlZLVlVkNFYxTjZaWGsyU0ZGWVJFWlpQUT09fDBmYTNmYWUyMTFmZTZhYWY0NWJhNjBkODAyNGFiZDdmMDc1OGEwYzZmNDUxOTE0NzVhMmVjYjNiMGYyODgyODY" />
              
              
                <label for="username_input">Username:</label>
                <input id="username_input"
                       
                       type="text"
                       autocapitalize="off"
                       autocorrect="off"
                       autocomplete="username"
                       class="form-control"
                       name="username"
                       value=""
                       autofocus="autofocus"
                        />
              
              
                <label for='password_input'>Password:</label>
                <input id="password_input"
                       
                       type="password"
                       class="form-control"
                       autocomplete="current-password"
                       name="password"
                        />
              
              
              <div class="feedback-container">
                <input id="login_submit"
                       type="submit"
                       class='btn btn-jupyter form-control'
                       value='Sign in'
                       tabindex="3" />
                <div class="feedback-widget hidden">
                  <i class="fa fa-spinner"></i>
                </div>
              </div>
              
                
              
            </div>
          </form>
        
      
    </div>
  

    
    
    
  
  
  <div class="modal fade"
       id="error-dialog"
       tabindex="-1"
       role="dialog"
       aria-labelledby="error-label"
       aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h2 class="modal-title" id="error-label">Error</h2>
          <button type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"></button>
        </div>
        <div class="modal-body">
      <div class="ajax-error alert-danger">The error</div>
    </div>
        <div class="modal-footer">
          <button type="button"
                  class="btn btn-primary"
                  data-bs-dismiss="modal"
                  data-dismiss="modal">OK</button>
        </div>
      </div>
    </div>
  </div>

    
  
    
  <script>
    if (!window.isSecureContext) {
      // unhide http warning
      var warning = document.getElementById('insecure-login-warning');
      warning.className = warning.className.replace(/\bhidden\b/, '');
    }
    // setup onSubmit feedback
    $('form').submit((e) => {
      var form = $(e.target);
      form.find('.feedback-container>input').attr('disabled', true);
      form.find('.feedback-container>*').toggleClass('hidden');
      form.find('.feedback-widget>*').toggleClass('fa-pulse');
    });
  </script>

  </body>
</html>
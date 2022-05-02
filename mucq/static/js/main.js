/* menu */

var menuList = document.getElementById('menu');

menuList.style.maxHeight = "0px";

function togglemenu() {
  if (menuList.style.maxHeight == "0px") {
    menuList.style.maxHeight = "130px";
  }
  else {
    menuList.style.maxHeight = "0px";
  }
}

/* languages */

var language = {
    eng: {
        home: 'Feed',
        support: 'Support',
        login: 'Login',
        sign_up: 'Sign Up',
        //logout: 'Logout',
        about: 'About',
    },
    chi: {
        home: '主頁',
        support: '協助',
        login: '登入',
        sign_up: '登記',
        //logout: '登出',
        about: '關於我們',
    },
};


if (window.location.hash) {
    if (window.location.hash === '#chi') {
      login.textContent = language.chi.login;
      sign_up.textContent = language.chi.sign_up;
      //logout.textContent = language.chi.logout;
      menuabout.textContent = language.chi.about;
      menuhome.textContent = language.chi.home;
      menusupport.textContent = language.chi.support;
    };
    if (window.location.hash === '#eng') {
      login.textContent = language.eng.login;
      sign_up.textContent = language.eng.sign_up;
      //logout.textContent = language.eng.logout;
      menuabout.textContent = language.eng.about;
      menuhome.textContent = language.eng.home;
      menusupport.textContent = language.eng.support;
    };
};
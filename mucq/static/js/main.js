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
        home: 'Home',
        support: 'Support',
        title: 'Title',
        content: 'Content',
        create: 'Create',
        mucq_title: 'Welcome to MucQ!',
        login: 'Login',
        sign_up: 'Sign Up',
        //logout: 'Logout',
        about: 'About', 
        intro: 'Welcome to MucQ! See what/s new!',
        log_in_reminder: 'You will have to log in to join the conversation!',
    },
    chi: {
        home: '主頁',
        support: '協助',
        title: '題目',
        content: '內容',
        create: '創造',
        login: '登入',
        sign_up: '登記',
        //logout: '登出',
        about: '關於我們',
        mucq_title: '歡迎光臨到 MucQ!',
        intro: '做 MucQ，講 MucQ，MucQ 都喺晒度！',
        log_in_reminder: '請先登入，然後再留言。',
    },
};


if (window.location.hash) {
    if (window.location.hash === '#chi') {
      login.textContent = language.chi.login;
      sign_up.textContent = language.chi.sign_up;
      //logout.textContent = language.chi.logout;
      home.textContent = language.chi.home;
      menu_about.textContent = language.chi.about;
      menu_home.textContent = language.chi.home;
      menu_support.textContent = language.chi.support;
      mucq_welcome.textContent = language.chi.mucq_title;
      mucq_welcome_message.textContent = language.chi.intro;
      create_post_title.textContent = language.chi.title;
      create_post_content.textContent = language.chi.content;
      log_in_reminder.textContent = language.chi.log_in_reminder;
    };
    if (window.location.hash === '#eng') {
      login.textContent = language.eng.login;
      sign_up.textContent = language.eng.sign_up;
      //logout.textContent = language.eng.logout;
      home.textContent = language.eng.home;
      menu_about.textContent = language.eng.about;
      menu_home.textContent = language.eng.home;
      menu_support.textContent = language.eng.support;
      mucq_welcome.textContent = language.eng.mucq_title;
      mucq_welcome_message.textContent = language.eng.intro;
      create_post_title.textContent = language.eng.title;
      create_post_content.textContent = language.eng.content;
      log_in_reminder.textContent = language.eng.log_in_reminder;
    };
};
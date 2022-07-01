var language = {
    eng: {
        home: 'Feed',
        title: 'Title',
        content: 'Content',
        create: 'Create',
        mucq_title: 'Welcome to MucQ!',
        intro: 'Welcome to MucQ! See what\'s new!',
        login_reminder: 'You will have to log in to join the conversation.',
    },
    chi: {
        home: '主頁',
        title: '題目',
        content: '內容',
        create: '創造',
        mucq_title: '歡迎光臨到 MucQ!',
        intro: '做 MucQ，講 MucQ，MucQ 都喺晒度！',
        login_reminder: '請先登入然後再留言。',
    },
};


if (window.location.hash) {
    if (window.location.hash === '#chi') {
      home.textContent = language.chi.home;
      mucq_welcome.textContent = language.chi.mucq_title;
      mucq_welcome_message.textContent = language.chi.intro;
      create_post_title.textContent = language.chi.title;
      create_post_content.textContent = language.chi.content;
      loginReminder.textContent = language.chi.login_reminder;
    };
    if (window.location.hash === '#eng') {
      home.textContent = language.eng.home;
      mucq_welcome.textContent = language.eng.mucq_title;
      mucq_welcome_message.textContent = language.eng.intro;
      create_post_title.textContent = language.eng.title;
      create_post_content.textContent = language.eng.content;
      loginReminder.textContent = language.eng.login_reminder;
    };
};
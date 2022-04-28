class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SECRET_KEY = '188db0c1a734f4d4d31f26f6c0ef5562d7aa4910caeb09b2bd402a25edba2d51b4000e2245f818c9e1216cb62e3e98761ebbaac40510ce4608213ef327e32e12322f02e423'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = True
    MAIL_USERNAME = 'mucq.contact@gmail.com'
    MAIL_PASSWORD = 'sussyimposter'

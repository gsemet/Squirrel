'use strict';

angular.module('squirrel').constant('AUTH_EVENTS', {
  loginSuccess: 'auth-login-success',
  loginFailed: 'auth-login-failed',
  logoutSuccess: 'auth-logout-success',
  sessionTimeout: 'auth-session-timeout',
  notAuthenticated: 'auth-not-authenticated',
  notAuthorized: 'auth-not-authorized'
})

angular.module('squirrel').constant('USER_ROLES', {
  all: '*',
  admin: 'admin',
  registered: 'registered',
  premium: 'premium',
})

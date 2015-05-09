 /*jshint unused:false */

 /***************

   This file allow to configure a proxy system plugged into BrowserSync
   in order to redirect backend requests while still serving and watching
   files from the web project

   IMPORTANT: The proxy is disabled by default.

   If you want to enable it, watch at the configuration options and finally
   change the `module.exports` at the end of the file

 ***************/

 'use strict';

 var httpProxy = require('http-proxy');
 var chalk = require('chalk');
 var historyApiFallback = require('connect-history-api-fallback')
 var enableHtml5ModeFallback = true;

 /*
  * Location of your backend server
  */
 var proxyTarget = 'http://localhost:8080/';

 var proxy = httpProxy.createProxyServer({
   target: proxyTarget
 });

 proxy.on('error', function(error, req, res) {
   res.writeHead(500, {
     'Content-Type': 'text/plain'
   });

   console.error(chalk.red('[Proxy]'), error);
 });

 /*
  * The proxy middleware is an Express middleware added to BrowserSync to
  * handle backend request and proxy them to your backend.
  */
 function proxyMiddleware(req, res, next) {
   /*
    * This test is the switch of each request to determine if the request is
    * for a static file to be handled by BrowserSync or a backend request to proxy.
    *
    * The existing test is a standard check on the files extensions but it may fail
    * for your needs. If you can, you could also check on a context in the url which
    * may be more reliable but can't be generic.
    */
   /* Default test:
    *
    *  /\.(html|css|js|png|jpg|jpeg|gif|ico|xml|rss|txt|eot|svg|ttf|woff|cur)(\?((r|v|rel|rev)=[\-\.\w]*)?)?$/
    */
   if (/^\/api\//.test(req.url)) {
     // route all request to /api/* to backend running on port 3000
     console.log("[serving w/ proxy] " + req.url);
     proxy.web(req, res);
   } else {
     if (enableHtml5ModeFallback) {
       console.log("[serving w/o proxy (html5mode fallback)] " + req.url);
       return historyApiFallback({
         verbose: false
       })(req, res, next);
     } else {
       console.log("[serving w/o proxy] " + req.url);
       next();
     }
   }

   /*
    * This is where you activate or not your proxy.
    *
    * The first line activate it and the second one ignored it
    */

   module.exports = [proxyMiddleware];
   //module.exports = [];
 }

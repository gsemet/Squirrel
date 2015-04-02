'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')();

var wiredep = require('wiredep').stream;

gulp.task('inject', ['styles'], function() {

  var injectIndexStyles = gulp.src([
    paths.tmp + '/serve/app/index.css',
  ], {
    read: false
  });

  var injectVendorStyles = gulp.src([
    paths.tmp + '/serve/app/vendor.css',
  ], {
    read: false
  });

  var injectScripts = gulp.src([
    paths.src + '/{app,components,services,directives}/**/*.js',
    paths.src + '/po/*.js',
    paths.src + '/index.js',
    '!' + paths.src + '/{app,components,services,directives}/**/*.spec.js',
    '!' + paths.src + '/{app,components,services,directives}/**/*.mock.js'
  ])
    .pipe($.angularFilesort());

  var injectIndexOptions = {
    ignorePath: [paths.src, paths.tmp + '/serve'],
    addRootSlash: false
  };
  var injectVendorOptions = {
    ignorePath: [paths.src, paths.tmp + '/serve'],
    addRootSlash: false,
    name: "vendor",
  };
  var injectScriptsOptions = {
    ignorePath: [paths.src, paths.tmp + '/serve'],
    addRootSlash: false
  };

  var wiredepOptions = {
    directory: 'bower_components',
    exclude: [/bootstrap\.js/, /bootstrap\.css/, /bootstrap\.css/,
              /foundation\.css/, /highcharts\.src\.js/, /toaster.min.js/]
  };

  var indexFilter = $.filter('index.css');
  var vendorFilter = $.filter('vendor.css');

  return gulp.src(paths.src + '/*.html')
    .pipe($.inject(injectIndexStyles, injectIndexOptions))
    .pipe($.inject(injectVendorStyles, injectVendorOptions))
    .pipe(vendorFilter.restore())
    .pipe($.inject(injectScripts, injectScriptsOptions))
    .pipe(wiredep(wiredepOptions))
    .pipe(gulp.dest(paths.tmp + '/serve'));

});

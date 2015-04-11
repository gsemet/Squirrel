'use strict';

var gulp = require('gulp');

var paths = gulp.paths;

var util = require('util');

var browserSync = require('browser-sync');

var middleware = require('./proxy');

function browserSyncInit(baseDir, files, browser) {
  browser = browser === undefined ? 'default' : browser;

  var routes = null;
  if (baseDir === paths.src || (util.isArray(baseDir) && baseDir.indexOf(paths.src) !== -1)) {
    routes = {
      '/bower_components': 'bower_components',
      '/node_modules': 'node_modules',
    };
  }

  browserSync.instance = browserSync.init(files, {
    startPath: '/',
    server: {
      baseDir: baseDir,
      middleware: middleware,
      routes: routes
    },
    browser: browser
  });
}

gulp.task('serve', ['watch'], function() {
  browserSyncInit([
    paths.tmp + '/serve',
    paths.src
  ], [
    paths.tmp + '/serve/{app,components,services,modules}/**/*.css',
    paths.src + '/{app,components,services,modules}/**/*.js',
    paths.src + '/po/*.js',
    paths.src + '/index.js',
    paths.src + 'src/assets/images/**/*',
    paths.tmp + '/serve/*.html',
    paths.tmp + '/serve/{app,components,services,modules}/**/*.html',
    paths.src + '/{app,components,services,modules}/**/*.html'
  ]);
});

gulp.task('serve:dist', ['build'], function() {
  browserSyncInit(paths.dist);
});

gulp.task('serve:e2e', ['inject'], function() {
  browserSyncInit([paths.tmp + '/serve', paths.src], null, []);
});

gulp.task('serve:e2e-dist', ['build'], function() {
  browserSyncInit(paths.dist, null, []);
});

/* global malarkey:false, moment:false */

import config from './index.config';
import routerConfig from './index.route';
import runBlock from './index.run';
import HomepageController from './views/homepage/homepage.controller';
/*import GithubContributorService from '../app/components/githubContributor/githubContributor.service';
import WebDevTecService from '../app/components/webDevTec/webDevTec.service';
import NavbarDirective from '../app/components/navbar/navbar.directive';
import MalarkeyDirective from '../app/components/malarkey/malarkey.directive';*/

angular.module('', ['ngAnimate', 'ngCookies', 'ngTouch', 'ngSanitize', 'ngMessages', 'ngAria', 'restangular',
    'ui.router', 'ui.bootstrap', 'toastr'])
  .constant('malarkey', malarkey)
  .constant('moment', moment)
  .config(config)
  .config(routerConfig)
  .run(runBlock)
  /*.service('githubContributor', GithubContributorService)
  .service('webDevTec', WebDevTecService)*/
  .controller('HomepageController', HomepageController)
  /*.directive('acmeNavbar', () => new NavbarDirective())
    .directive('acmeMalarkey', () => new MalarkeyDirective(malarkey));*/

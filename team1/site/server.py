# -*- coding: utf-8 -*-

from bottle import route, run, template


code = """"
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

  <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:og="http://opengraphprotocol.org/schema/">
    <head>

    <title>Home | Mail Online</title>


    <meta name="keywords" content="Sudoku, horoscopes, political analysis, news, Don't Miss, pictures, comment, Daily Mail, Mail on Sunday newspapers, sport, Westminster, opinion" />
    <meta name="description" content="MailOnline - all the latest news, sport, showbiz, science and health stories from around the world from the Daily Mail and Mail on Sunday newspapers" />
    <meta name="robots" content="noodp,noydir,all" />
    <meta name="dartPageType" content="hp" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="Content-Language" content="en" />
    <meta name="Rating" content="General" />
    <meta name="doc-class" content="Living Document" />
    <meta name="verify-v1" content="DXwlrsxbqxSv+FTFkWUfgflBvFJfx2YbNf/HmABrVyY=" />
    <meta name="msvalidate.01" content="12E6B4B813EB44C9BFC8F6A21F1D01F5" />
    <meta name="y_key" content="1a7e912afbfcab2f" />
    <meta http-equiv="imagetoolbar" content="false" />
    <meta name="MSSmartTagsPreventParsing" content="true" />
    <meta property="twitter:account_id" content="15438913" />
    <meta property="fb:app_id" content="146202712090395" />
    <meta property="og:site_name" content="Mail Online" />
    <meta property="og:title" content="Home | Mail Online" />
    <meta property="og:type" content="website" />
    <meta property="og:description" content="MailOnline - all the latest news, sport, showbiz, science and health stories from around the world from the Daily Mail and Mail on Sunday newspapers" />
    <meta property="og:url" content="http://www.dailymail.co.uk/home/index.html" />
    <meta property="og:image" content="http://i.dailymail.co.uk/i/social/img_mol-logo_50x50.png" />
    <meta name="application-name" content="MailOnline" />
    <meta name="msapplication-tooltip" content="MailOnline" />
    <meta name="msapplication-starturl" content="/" />
    <meta name="msapplication-task" content="name=Register to Comment;action-uri=https://register.dailymail.co.uk/startRegister;icon-uri=http://i.dailymail.co.uk/i/furniture/ie9/jmplstic_register.ico" />
    <meta name="msapplication-task" content="name=Login;action-uri=https://register.dailymail.co.uk/login?redirectPath=http://www.dailymail.co.uk;icon-uri=http://i.dailymail.co.uk/i/furniture/ie9/jmplstic_login.ico" />
    <meta name="msapplication-task" content="name=Debate;action-uri=/debate/index.html;icon-uri=http://i.dailymail.co.uk/i/furniture/ie9/jmplstic_debate.ico" />
    <meta name="msapplication-task" content="name=Columnists;action-uri=/debate/columnists/index.html;icon-uri=http://i.dailymail.co.uk/i/furniture/ie9/jmplstic_debate.ico" />

    <link rel="canonical" href="http://www.dailymail.co.uk/home/index.html"   />
    <link rel="search" href="/xml/opensearch.xml" title="Mail Online Search" type="application/opensearchdescription+xml" />
    <link rel="alternate" href="/home/index.rss" title="Mail Online Home RSS feed" type="application/rss+xml" />
    <link rel="publisher" href="https://plus.google.com/101913233771349778690/"   />

    
    
    

    <link rel="stylesheet" type="text/css" media="screen" href="http://scripts.dailymail.co.uk/static/gunther/gunther-535/all--.css" /><link rel="stylesheet" type="text/css" media="screen" href="http://scripts.dailymail.co.uk/static/gunther/gunther-535/all1--.css" />
  <link rel="stylesheet" type="text/css" media="screen" href="http://scripts.dailymail.co.uk/static/gunther/gunther-535/colours.css" />
  <link rel="stylesheet" type="text/css" media="screen" href="http://scripts.dailymail.co.uk/static/gunther/gunther-535/mobilegallery--.css" />

  <!--[if lte IE 6]><link rel="stylesheet" type="text/css" media="screen" href="http://scripts.dailymail.co.uk/static/gunther/gunther-535/ie6--.css" /><![endif]-->

  <link rel="stylesheet" type="text/css" media="print" href="http://scripts.dailymail.co.uk/static/gunther/gunther-535/print--.css" />

  <link rel="stylesheet" type="text/css" media="screen" href="http://scripts.dailymail.co.uk/static/gunther/gunther-440/registration--.css" />



  <style type="text/css">
  .homehome .masthead {
  background-image:url(http://i.dailymail.co.uk/i/pix/channelheaders/search_masthead.gif);
  }
  </style>


    <script type="text/javascript">
    PageCriteria = window.PageCriteria || {};
    PageCriteria.channel = 'home';
    PageCriteria.subchannel = 'home';
    PageCriteria.geo = 'GB';
    PageCriteria.pageType = 'channel';
    </script>
    
    <script type="text/javascript">
    PageCriteria.latitude = "50.90";
    PageCriteria.longitude = "-1.40";
    PageCriteria.geo = "GB" || PageCriteria.geo;
    </script>
    

    <script type="text/javascript">
      
        
          var twitterVia = 'MailOnline';
      
    
      var useAdx = false;
      var useFreewheel = false;
      var useRtp = false;  
    </script>
    <!-- Grapeshot-->
    <script type="text/javascript">
    var andGrapeshot,
        gs_channels = "DEFAULT",
        gs_us_channels = "DEFAULT";
    
    andGrapeshot = 1;
    
    </script>
    <script type='text/javascript'>
    var crtg_nid="1867";
    var crtg_cookiename="cto_dailymail";
    var crtg_varname="crtg_content";
    function crtg_getCookie(c_name){ var i,x,y,ARRCookies=document.cookie.split(";");for(i=0;i<ARRCookies.length;i++){x=ARRCookies[i].substr(0,ARRCookies[i].indexOf("="));y=ARRCookies[i].substr(ARRCookies[i].indexOf("=")+1);x=x.replace(/^\s+|\s+$/g,"");if(x==c_name){return unescape(y);}}return'';}
    
    var crtg_content = crtg_getCookie(crtg_cookiename);
    var crtg_rnd=Math.floor(Math.random()*99999999999);
    var crtg_url=location.protocol+'//rtax.criteo.com/delivery/rta/rta.js?netId='+escape(crtg_nid);crtg_url+='&cookieName='+escape(crtg_cookiename);crtg_url+='&rnd='+crtg_rnd;crtg_url+='&varName=' + escape(crtg_varname);
    var crtg_script=document.createElement('script');crtg_script.type='text/javascript';crtg_script.src=crtg_url;crtg_script.async=true;
    if(document.getElementsByTagName("head").length>0)document.getElementsByTagName("head")[0].appendChild(crtg_script);else if(document.getElementsByTagName("body").length>0)document.getElementsByTagName("body")[0].appendChild(crtg_script);</script>
    
    <script type="text/javascript">
      if (!window.console) window.console = { log: function() {} };
      var ANDDebugOn = false;
      var s_account='anddailymailprod';
      var s_account15 = 'molglobalprod';
    </script>
    
    <script type="text/javascript">
    
    
       var mol_ipad_smartappbanner = false;
      
    
      
        var mol_smartappbanner = true;
      
    
    </script>
    <script type="text/javascript" src="http://scripts.dailymail.co.uk/static/gunther/lib-4/lib--.js" ></script>
    <script type="text/javascript" src="http://scripts.dailymail.co.uk/static/gunther/gunther-535/dm1--.js" ></script>
    <script type="text/javascript">
      DM.guntherBase = 'http://scripts.dailymail.co.uk/static/gunther/gunther-535/';
      //features
      DM.features = {};
    </script>
    <script type="text/javascript">
    
    
      
        DM.isLoggedIn = false;
      
    
    </script>
    
    <script type="text/javascript">
    var adReferrer = '';
    
    if ("" != "") {
      DM.setCookie("adReferrer", "", "", "/");
      adReferrer = "";
    }
    else if (DM.getCookie("adReferrer") != null) {
      adReferrer = DM.getCookie("adReferrer");
    }
    
    var adType='dart',
        dartSiteId = "dailymail.uk",
        DFPid="N5765",
        adAreaSiteId = "dm",
        adAreaId = "home",
        adSubareaId = (adReferrer == "") ? "home" : adReferrer,
      adPageType = 'hp',
      adContent = "",
      adSection = '',
      adArticleId = "",
      adEnvironment = "production",
      enableAds=true;
    
    </script>
    
      <script type="text/javascript">
          var freewheelAdIdentType = "standardBC_id";
          function setFreewheelAdIdentType (id) {
              if (window.useFreewheel && id) {
                  freewheelAdIdentType = "mi9videoid";
              } else if (window.useFreewheel) {
                  freewheelAdIdentType = "standardBC_id";
              }
          }
      
          if (window.useFreewheel) {
              window.fw_config = function() {
                  return _.chain({
                      siteSection: 'dma_home',
                      siteSectionId: 'dma_home',
                      assetIdField: freewheelAdIdentType
                  }).extend({     amLocation: "http://adm.fwmrm.net/p/msn_au_live/AdManager.swf",         amLocation_js: "http://adm.fwmrm.net/p/msn_au_live/AdManager.js", cb_profile: "MSN_AU_BC_Live",     cb_profile_js: "MSN_AU_BC_HTML5_Live",     fw_server: "http://5bb3d.v.fwmrm.net",     networkId: 375613,    videoAssetFallbackId:"brightcove_video"   } ).value();
              };
          }
      </script>

    

    <script type="text/javascript">
    var taboola_country = 'uk';
    window._taboola = window._taboola || [];
    _taboola.push({ home:'auto' });
    !function (e, f, u) {
      e.async = 1;
      e.src = u;
      f.parentNode.insertBefore(e, f);
    }(document.createElement('script'), document.getElementsByTagName('script')[0], 'http://cdn.taboola.com/libtrc/dailymail-' + taboola_country + '/loader.js');
  </script>


    <!--[if gte IE 8]><!-->
  <link rel="stylesheet" type="text/css" media="screen" href="http://scripts.dailymail.co.uk/static/gunther/gunther-535/fff.css">
  <!--<![endif]-->


  </head>

    <body id="home" class="homehome mol-desktop">
      <script type="text/javascript">MobileUtils.setupMobileClass();</script>
    
      <script type="text/javascript">
    //<![CDATA[
    DM.ComScore.off = false;
    DM.ComScore.labels = {
      c2: '14366613',
      name: 'home.home.page',
      mo_vs_pl: 'we',
      mo_vs_pr: 'dm',
      mo_vs_ct: 'ho',
      category: 'home',
      mo_site: 'dailymail',
      mo_logged_in: 0
    }
    if (DM.isLoggedIn && DM.userId) {
      Ext.apply(DM.ComScore.labels, {
        mo_logged_in: 1,
        mo_user_id: DM.userId
      });
    }
    DM.ComScore.dm  = DM.ComScore.getDM();
    DM.ComScore.vd  = '';
    //]]>
  </script>

  <!-- Begin comScore Inline Tag 1.1111.15 -->
  <script type="text/javascript">
    //<![CDATA[
    function udm_(a) {
      var b = "comScore=", c = document, d = c.cookie, e = "", f = "indexOf", g = "substring", h = "length", i = 2048, j, k = "&ns_", l = "&", m, n, o, p, q = window, r = q.encodeURIComponent || escape;
      if (d[f](b) + 1)for (o = 0, n = d.split(";"), p = n[h]; o < p; o++)m = n[o][f](b), m + 1 && (e = l + unescape(n[o][g](m + b[h])));
      a += k + "_t=" + +(new Date) + k + "c=" + (c.characterSet || c.defaultCharset || "") + "&c8=" + r(c.title) + e + "&c7=" + r(c.URL) + "&c9=" + r(c.referrer), a[h] > i && a[f](l) > 0 && (j = a[g](0, i - 8).lastIndexOf(l), a = (a[g](0, j) + k + "cut=" + r(a[g](j + 1)))[g](0, i)), c.images ? (m = new Image, q.ns_p || (ns_p = m), m.src = a) : c.write("<", "p", "><", 'img src="', a, '" height="1" width="1" alt="*"', "><", "/p", ">")
    }
    udm_('http' + (document.location.href.charAt(4) == 's' ? 's://sb' : '://b') + '.scorecardresearch.com/b?c1=2&c2=' + '14366613' + '&name=' + 'home.home.page' + '&mo_vs_pl=we&mo_vs_pr=dm&mo_vs_ct=ho&mo_tb=0&category=home&mo_site=dailymail' + ((DM.isLoggedIn && DM.userId) ? '&mo_logged_in=1&mo_user_id=' + DM.userId : '&mo_logged_in=0') + DM.ComScore.dm + DM.ComScore.vd);
    //]]>
  </script>

  <noscript><p><img src="http://b.scorecardresearch.com/p?c1=2&c2=14366613&name=home.home.page&mo_vs_pl=we&mo_vs_pr=dm&mo_vs_ct=ho&mo_tb=0&category=home&mo_site=dailymail&mo_logged_in=0" height="1" width="1" alt="*"></p></noscript>
  <!-- End comScore Inline Tag -->

          <!-- SiteCatalyst code version: H.20.3.
      Copyright 1997-2009 Omniture, Inc. More info available at
      http://www.omniture.com -->

      <script type="text/javascript">
        var searchTerms = '';
      </script>

      
      
      <script type="text/javascript">
        searchTerms = '';
      </script>
      
      

      <script type="text/javascript"><!--
      var refererHost = "direct";
      if (document.referrer) {
          var docReferrerHostMatches = new RegExp("://([^/]*)/.*").exec(document.referrer);
          /* Check just to be safe */
          if (docReferrerHostMatches) {
              var docReferrerHost = docReferrerHostMatches[1];
              refererHost = docReferrerHost;
          }
      }
      // login tracking (1)
      DM.pageEvents.listen(DM.pageEvents.PAGE_LOGIN_BUTTON_CLICKED, function (obj, event, pars){
          if (pars.action === 'loggingIn'){
              document.cookie = "attempting_login=true; path=/";
          }
      });

      DM.setPageMetadata((function (){
          var pagemeta = {
              domain: 'dailymail',
              channel: '/home',
              subChannel: '' || '/home',
              subChannel2: '',
              contentType: '' || 'home',
              articleTitle: '',
              articleId: '',
              articleVersionNumber: '',
              internalSearchTerms: searchTerms,
              loggedInStatus: (DM.isLoggedIn ? 'Logged In' : 'Logged Out'),
              galleryTitle: '',
              galleryId: '',
              threadTitle: '',
              threadId: '',
              userId: DM.userId,
              partnerSite: '',
              publishedDate: null,
              authorName: '',
              errorUrl: '',
              serverDate: new Date(1399575688064),
              url: 'D=g',
              referringSubDomain: refererHost,
              inlineLinks: '',
              pageName: '' || '/home/home',
              products: '',
        bundleVersion: 'gunther-535'
          };
          // login tracking (1)
          if (document.cookie.replace(/(?:(?:^|.*;\s*)attempting_login\s*\=\s*([^;]*).*$)|^.*$/, "$1") === "true" &&
              DM.isLoggedIn) {
                document.cookie = "attempting_login=false; path=/";
                pagemeta.registrationEntry = 'Successfully Logged In';
          }

          return pagemeta;
      }()));

      /************* DO NOT ALTER ANYTHING BELOW THIS LINE ! **************/
      DM.pageEvents.fireEvent(DM.pageEvents.PAGE_RENDER_STARTED, DM.getPageMetadata());
      //--></script>
      <script type="text/javascript"><!--
      if(navigator.appVersion.indexOf('MSIE')>=0)document.write(unescape('%3C')+'\!-'+'-')
      //--></script><!--/DO NOT REMOVE/-->
      <!-- End SiteCatalyst code version: H.20.3. -->

          <script type="text/javascript">
           
          var _gaq = _gaq || [];
            _gaq.push(['_setAccount', 'UA-3639451-1']);
            _gaq.push(['_trackPageview']);
      
            (function() {
              var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
              ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
              (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
            })();
          </script>
      
      
      <script type="text/javascript">
        if (!DM.ted) {
          DM.ted = {
            geo: function(location) {
              DM.ted.g = location;
            }
          };
        }
        
        
            DM.ted.geo('GB');
          
        
        if (!DM.ted.tedEvent) {
          AND.addScript('http://video.dailymail.co.uk/brightcove/tracking/ted3.js', {
            success: function() {
            }
          });
        } else {
        }
      </script>
      <script type="text/javascript">
      (function() {
        var currentChannel = 'home' || 'none';
        var subchannel = 'home' || 'none';
        var currentSubchannel = (subchannel === currentChannel) ? 'none' : subchannel;
        var pageType = 'channel';
      
        var adControlDevice = "";
        if (MobileUtils.isIPhone()) {
          adControlDevice = "iphone";
        } else if (MobileUtils.isIPad()) {
          adControlDevice = "ipad";
        } else if (MobileUtils.isAndroidTablet() || MobileUtils.isKindleSilk()) {
          adControlDevice = "androidTablet";
        } else if (MobileUtils.isAndroidPhone()) {
          adControlDevice = "androidMobile";
        } else {
          adControlDevice = "other";
        }
        var url = 'http://mads.dailymail.co.uk/v2' + '/' + PageCriteria.geo.toLowerCase() + '/' + currentChannel + '/' + currentSubchannel + '/' + pageType + '/' + adControlDevice;
      
        adverts.setStickyBannerZoomThresholds(
          1,
          1
        );
        adverts.requestSlotConfig(url);
      })();
      </script>    
      <script>(function() {
        var _fbq = window._fbq || (window._fbq = []);
        if (!_fbq.loaded) {
          var fbds = document.createElement('script');
          fbds.async = true;
          fbds.src = '//connect.facebook.net/en_US/fbds.js';
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(fbds, s);
          _fbq.loaded = true;
        }
        _fbq.push(['addPixelId', '1401367413466420']);
      })();
      window._fbq = window._fbq || [];
      window._fbq.push(["track", "PixelInitialized", {}]);
      </script>
      <noscript><img height="1" width="1" border="0" alt="" style="display:none" src="https://www.facebook.com/tr?id=1401367413466420&amp;ev=NoScript" /></noscript>
    
       <div id="adx_page_skins" class="adHolder">
           <script type="text/javascript">
              adverts.addToArray({pos: 'adx_page_skins'});
          </script>
      </div>  
      <div id="lightbox-target" class="lightbox-gallery hidden"></div>
      <div id="top" class="page_banner_overrides page page-banner ">
        





  <div id="page-container">
        <div class="clear">&nbsp;</div>

        <div class="page-header bdrgr2">
    <div class="home">
      <div class="masthead">
        <a href="/"><img src="http://i.dailymail.co.uk/i/sitelogos/logo_mol.gif" width="350" height="66" alt="MailOnline - news, sport, celebrity, science and health stories" id="logo" /></a>
      </div>
  </div>
  <a name="navigation"></a>
      <ul class="nav-primary  cleared bdrgr3 cnr5"
          data-track-module="nav-primary^primary" data-track-pos="static">
        <li class="home">
    <span class="tl">&nbsp;</span>
    <span class="tr">&nbsp;</span>
    <span class="link-wocc linkro-wocc">
      <a href="/home/index.html" >Home</a>
    </span>
  </li>

  <li class="news">
    <span class="link-gr6ox linkro-ccox">
      <a href="/news/index.html" class="no-border" > News</a>
    </span>
  </li>

  <li class="home">
    <span class="link-gr6ox linkro-ccox">
      <a href="/ushome/index.html"  > U.S.</a>
    </span>
  </li>

  <li class="sport">
    <span class="link-gr6ox linkro-ccox">
      <a href="/sport/index.html"  > Sport</a>
    </span>
  </li>

  <li class="tvshowbiz">
    <span class="link-gr6ox linkro-ccox">
      <a href="/tvshowbiz/index.html"  > TV&amp;Showbiz</a>
    </span>
  </li>

  <li class="femail">
    <span class="link-gr6ox linkro-ccox">
      <a href="/femail/index.html"  > Femail</a>
    </span>
  </li>

  <li class="health">
    <span class="link-gr6ox linkro-ccox">
      <a href="/health/index.html"  > Health</a>
    </span>
  </li>

  <li class="sciencetech">
    <span class="link-gr6ox linkro-ccox">
      <a href="/sciencetech/index.html"  > Science</a>
    </span>
  </li>

  <li class="money">
    <span class="link-gr6ox linkro-ccox">
      <a href="/money/index.html"  > Money</a>
    </span>
  </li>

  <li class="video">
    <span class="link-gr6ox linkro-ccox">
      <a href="/video/index.html"  > Video</a>
    </span>
  </li>

  <li class="coffeebreak">
    <span class="link-gr6ox linkro-ccox">
      <a href="/coffeebreak/index.html"  > Coffee Break</a>
    </span>
  </li>

  <li class="travel">
    <span class="link-gr6ox linkro-ccox">
      <a href="/travel/index.html"  > Travel</a>
    </span>
  </li>

  <li class="femail">
    <span class="link-gr6ox linkro-ccox">
      <a href="/femail/fashionfinder/index.html"  > Fashion Finder</a>
    </span>
  </li>


      </ul>

  <div class="home">
    <div class="nav-secondary  wocc link-lccox cleared bdrgr3"
      data-track-module="nav-secondary^secondary" data-track-pos="static">
      <ul class="float-l">
        <li class="first">
          <a href="/home/latest/index.html"  >Latest headlines</a>
        </li>
        <li class="">
          <a href="/home/you/index.html"  >You mag</a>
        </li>
        <li class="">
          <a href="/home/event/index.html"  >Event</a>
        </li>
        <li class="">
          <a href="/home/books/index.html"  >Books</a>
        </li>
        <li class="">
          <a href="/home/prmts/index.html"  >Promos</a>
        </li>
        <li class="">
          <a href="https://mailrewardsclub.mailonline.co.uk/WeekendClub/" target="_blank" >Rewards</a>
        </li>
        <li class="">
          <a href="http://www.mailgardenshop.co.uk" target="_blank" >Mail Garden</a>
        </li>
        <li class="">
          <a href="http://www.dailymail.pinkribbonbingo.com/?a=11310index.html"  >Bingo</a>
        </li>
        <li class="">
          <a href="/coffeebreak/horoscopes/"  >Horoscopes</a>
        </li>
        <li class="">
          <a href="/property/index.html"  >Property</a>
        </li>
        <li class="">
          <a href="/motoring/index.html"  >Motoring</a>
        </li>
        <li class="">
          <a href="/columnists/index.html"  >Columnists</a>
        </li>
        <li class="">
          <a href="/home/stats/index.html"  >Stats</a>
        </li>
      </ul>

      <script language="JavaScript">
          <!--
          if (DM.isLoggedIn) {
              document.write('<ul class="float-r">      <li class="first">        <a href="/registration/profile.html">My Profile</a>      </li>      <li id="logout" class="first">        <a class="js-logout" href="/registration/logout.html">Logout</a>      </li>    </ul>');
              } else {
          document.write('<ul class="float-r">      <li id="login" class="first">        <a class="js-login" href="/registration/login.html?targetUrl= "           data-target="/registration/p/lightbox_login.html?targetUrl= .login-lightbox"           data-modal-type="login-overlay"           data-ajax-refresh-everytime="false"           data-toggle="modal">Login</a>      </li>    </ul>');
          }
          // -->
      </script>

        <noscript>
            <ul class="float-r">      <li class="first">        <a href="/registration/profile.html">My Profile</a>      </li>      <li id="logout" class="first">        <a class="js-logout" href="/registration/logout.html">Logout</a>      </li>    </ul>
        </noscript>

        <!-- to remove after releasing gunther -->
      <script type="text/javascript">
      DM.has('login', 'login', {
        url: '/registration/p/lightbox_login.html?targetUrl=' + window.location
      });
      DM.has('logout', 'logout', {
        url: '/registration/logout.html?targetUrl=' + window.location
      });
      </script>
    </div>
  </div>

  <script>
  currentChannelTwitterFollow = 'MailOnline';
  NavigationShare.init({facebookAppId: '146202712090395',
              facebookChannelUrl: 'http://www.dailymail.co.uk/facebook/channel.html',
              channel: '',
              hostName: 'http://www.dailymail.co.uk',
              articleUrl: ''});
  </script>

  <div class="supplements"
    data-track-module="nav-supplements^supplements" data-track-pos="static">
    <div class="lkeFlw">
      <div class="imgs">
       </div>
        <div class="links">
    <a href="http://www.dailymail.co.uk/home/article-1388040/Privacy-Policy-Cookies.html"  target="_blank"  >Cookie Policy</a>
    <a href="/home/feedback.html"   class="last" >Feedback</a>
  </div>

      <div class="btns">
        <div class="fb-like" data-href="http://www.facebook.com/DailyMail" data-send="false" data-layout="button_count" data-width="150" data-show-faces="false" data-font="arial"></div>
      </div>
      <div class="btns">
        <a style="border-right:none;" href="https://twitter.com/MailOnline" class="twitter-follow-button twitter-follow-header" data-show-count="false" data-show-screen-name="true"></a>
      </div>
      <div class="btns pinterest-follow-button">
        <a data-pin-do="buttonFollow" rel="nofollow" no href="http://www.pinterest.com/dailymail/">DailyMail</a>
      </div>
    </div>
    <div id="fb-root"></div>
  </div>

  <div class="weather" data-track-module="nav-weather^weather" data-track-pos="static"></div>
  <script type="text/javascript">
      var now = moment();
      $.get( "/weather.html", {
        old: "true",
        latitude: PageCriteria.latitude,
        longitude: PageCriteria.longitude,
        weatherDate: now.format('YYYYMMDDHH')}, function( data ) {
       $( ".page-header .weather" ).append( "<strong>" + now.format("dddd, MMM Do YYYY") + "</strong>" + data );
        });
  </script>

  </div> <!-- from masthead -->




        
        <div id="content">
        <div class="billboard_wrapper relative">
          <div class="adHolder billboard" id="billBoard">
            <script type="text/javascript">
            adverts.addToArray({pos:'billboard', type: "970x250,900x250", dcopt:true, adProbe: true});
            </script>
          </div>
          <div class="billboard-show js-show hdn">
            <a href="#" class="homeblue"><b class="arrow-small-d"></b> show ad</a>
          </div>
        </div>  
          <div class="gamma">
        <div class="article article-tri-headline ">
    <h2 class="linkro-darkred"><a href="#">{{headline1}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623480/The-Cold-War-really-IS-Russian-aircraft-carrier-group-Soviet-era-ships-escorted-English-Channel-state-art-Royal-Navy-destroyer.html">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623480-1DACD0D800000578-8_964x462.jpg" height="462" width="964" alt="Escort: HMS Dragon (foreground) with the Russian aircraft carrier 'Admiral Kuznetsov', in the English Channel. HMS Dragon tracked and met up with a Russian task group off the coast of Brest as they entered the English Channel yesterday" />
      </a>
      <div >
        <p>
          
          The seven-strong naval task group led by the Admiral Kuznetsov (pictured top), Russia's largest warship, entered the Channel last night, a Royal Navy spokesman said. Although the ships did not enter UK territorial waters, their movements were tracked by the Royal Navy destroyer HMS Dragon (pictured in foreground) - the duty fleet-ready escort vessel - which was dispatched from Portsmouth to investigate. The Russian Kirov Class battlecruiser 'Pyotr Velikiy' was also in the group.
        </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623480/The-Cold-War-really-IS-Russian-aircraft-carrier-group-Soviet-era-ships-escorted-English-Channel-state-art-Royal-Navy-destroyer.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623480">         558</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623480/The-Cold-War-really-IS-Russian-aircraft-carrier-group-Soviet-era-ships-escorted-English-Channel-state-art-Royal-Navy-destroyer.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuPRek| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623480-1DAD457D00000578-209_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

  </div>
    <div class="gamma">
        <div class="home item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

  </div>
    <div class="cleared">
        <div class="alpha">
     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-large cleared">
    <h2 class="linkro-darkred"><a href="#">{{headline2}}</a>
    </h2>
    <a href="/news/article-2623545/I-hope-girls-alive-reunited-parents-Sir-Bob-Geldof-speaks-publicly-time-Peaches-death-addresses-plight-Nigerian-schoolgirl-hostages.html">
        <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623545-1DAD2D9200000578-907_308x342.jpg" height="342" width="308" alt="Sir Bob Geldof has spoken publicly for the first time since the death of his daughter Peaches - to speak of the plight of the Nigerian schoolgirls taken hostage by terrorists" />
    </a>
    <div class="articletext-holder">
      <p>
        
        Michelle Obama, Malala Yousafzai, Hillary Clinton, and Amy Poehler are among those lending their support to the social media campaign, which encourages military intervention to recover the girls who were kidnapped from their school by Boko Haram rebels in north-east Nigeria.
      </p>
      <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623545/I-hope-girls-alive-reunited-parents-Sir-Bob-Geldof-speaks-publicly-time-Peaches-death-addresses-plight-Nigerian-schoolgirl-hostages.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623545">          13</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mGaHG4| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623545-1DAD2D9200000578-305_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

    </div>
  </div>


          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline3}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623275/Forget-carjacking-big-threat-car-HACKING-Thousands-vehicles-stolen-using-cheap-gadgets-bought-online.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623275-1DAAEE8700000578-591_154x115.jpg" height="84" width="112" alt="Figures from the Metropolitan Police Service claim half of car thefts in London last year were committed without force. It is thought criminals used hi-tech gadgets designed for locksmiths to gain access, instead. The gadgets can be bought online and there are video tutorials showing how to use them. Stock image pictured" />
      </a>
      <p>
        
        Figures from London's Metropolitan Police Service claim half of car thefts were carried out using hi-tech gadgets designed for locksmiths bought cheaply online.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623275/Forget-carjacking-big-threat-car-HACKING-Thousands-vehicles-stolen-using-cheap-gadgets-bought-online.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623275">         118</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFkHPL| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623275-1DAAEE8700000578-331_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="news item">
    <div class="image-swap-carousel cleared" id="p-78"
       data-track-module="gallery-1000003^image_swap_carousel"
       data-track-selector=".gallery-frame a, .scroller a">
    <h3 class="gr4ox">Click through today in pictures</h3>
    <div class="carousel-holder ccox">
      <div class="carousel horizontal bdrgr3">
        <div class="gallery-frame">
          <a class="js-link link" href="/tvshowbiz/article-2623386/Lenny-Henry-shows-results-drastic-three-stone-weight-loss-steps-London-looking-dapper.html">
            <img class="js-placeholder placeholder" src="http://i.dailymail.co.uk/i/pix/2014/01_01/Lenny-Henry_302x322.jpg" width="302" height="322" alt=""/>
            <span class="js-caption caption wogr6">
                Lean-ny Henry! Comic trim after losing three stone
            </span>
          </a>
        </div>
        <div class="scroller">
          <ul class="itemlist link-gr5ox js-itemList">
                <li>
                  <a rel="http://i.dailymail.co.uk/i/pix/2014/05_01/LilyAllen232_302x322.jpg| nofollow" href="/tvshowbiz/article-2623245/Lily-Allen-shares-snap-drip-saying-down.html">
                    <img src="http://i.dailymail.co.uk/i/pix/2014/05_01/LilyAllen23_83x60.jpg" height="60" width="83" alt="Ailing Lily tweets selfie from her hospital bed" />
                    <span class="xogr2">Lily</span>
                  </a>
                </li>
                <li>
                  <a rel="http://i.dailymail.co.uk/i/pix/2014/01_01/Lenny-Henry_302x322.jpg| nofollow" href="/tvshowbiz/article-2623386/Lenny-Henry-shows-results-drastic-three-stone-weight-loss-steps-London-looking-dapper.html">
                    <img src="http://i.dailymail.co.uk/i/pix/2014/01_01/Lenny-Henry_83x60.jpg" height="60" width="83" alt="Lean-ny Henry! Comic trim after losing three stone" />
                    <span class="xogr2">Lenny Henry</span>
                  </a>
                </li>
                <li>
                  <a rel="http://i.dailymail.co.uk/i/pix/2014/05_01/JessicaEnnis_302x322.jpg| nofollow" href="/tvshowbiz/article-2623353/My-abs-look-little-different-Jessica-Ennis-Hill-compares-baby-bump-famous-Olympic-six-pack.html">
                    <img src="http://i.dailymail.co.uk/i/pix/2014/05_01/JessicaEnnisCloseUP2_83x60.jpg" height="60" width="83" alt="'My abs look different': Jessica's baby bump" />
                    <span class="xogr2">Jessica</span>
                  </a>
                </li>
                <li>
                  <a rel="http://i.dailymail.co.uk/i/pix/2014/01_04/RonaldoandSon_302x322.jpg| nofollow" href="/tvshowbiz/article-2623465/Cristiano-Ronaldo-adorable-son-coordinate-white-hats-shades-enjoy-day-Madrid-Open.html">
                    <img src="http://i.dailymail.co.uk/i/pix/2014/01_04/RonaldoandSon_83x60.jpg" height="60" width="83" alt="We're matching daddy! Ronaldo and son coordinate hats" />
                    <span class="xogr2">Ronaldo</span>
                  </a>
                </li>
                <li>
                  <a rel="http://i.dailymail.co.uk/i/pix/2014/05_01/LilyAllen232_302x322.jpg| nofollow" href="/tvshowbiz/article-2623245/Lily-Allen-shares-snap-drip-saying-down.html">
                    <img src="http://i.dailymail.co.uk/i/pix/2014/05_01/LilyAllen23_83x60.jpg" height="60" width="83" alt="Ailing Lily tweets selfie from her hospital bed" />
                    <span class="xogr2">Lily</span>
                  </a>
                </li>
                <li>
                  <a rel="http://i.dailymail.co.uk/i/pix/2014/01_01/Lenny-Henry_302x322.jpg| nofollow" href="/tvshowbiz/article-2623386/Lenny-Henry-shows-results-drastic-three-stone-weight-loss-steps-London-looking-dapper.html">
                    <img src="http://i.dailymail.co.uk/i/pix/2014/01_01/Lenny-Henry_83x60.jpg" height="60" width="83" alt="Lean-ny Henry! Comic trim after losing three stone" />
                    <span class="xogr2">Lenny Henry</span>
                  </a>
                </li>
          </ul>
        </div>
        <div class="paging-controls">
          <a class="next js-move-next" href="#">
            <span class="usability">Next</span>
          </a>
          <a class="previous js-move-prev" href="#">
            <span class="usability">Previous</span>
          </a>
        </div>
      </div>
    </div>
  </div>
  <script type="text/javascript">
  DM.has("p-78", 'imageSwapCarousel');
  </script>
  </div>
  <script type="text/javascript">
    DM.has('p-78', 'comScore', {
      mo_mod_id: '1000003',
      mo_mod_pos: 'p-78'
    });
  </script>

          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline4}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623626/Mother-neo-Nazi-teen-compared-Sandy-Hook-school-killer-plotted-Columbine-style-massacre.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623626-1DACEF0600000578-989_156x117.jpg" height="84" width="112" alt="The Old Bailey heard that Michael Piggin, pictured here, was branded a future mass killer by his own mother" />
      </a>
      <p>
        
        A teenager from Loughborough accused of plotting a ‘new-Columbine’ massacre was branded a future mass killer by his own mother, the Old Bailey heard today.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="videos-link" href="/news/article-2623626/Mother-neo-Nazi-teen-compared-Sandy-Hook-school-killer-plotted-Columbine-style-massacre.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RvfwDR| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623626-1DACEF0600000578-40_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline5}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623606/Bipolar-stalker-harassed-father-toddler-went-missing-1981-having-pretending-daughter-despite-court-order-stay-away.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAD906B00000578-588_154x115.jpg" height="84" width="112" alt="Dated: 08/05/2014   \nWOMAN WHO HARASSED MISSING GIRL'S FAMILY\nA collect image of missing toddler Katrice Lee, who went missing in Germany over 30 years ago in 1981.  \nsee court case  Donna Wright was ordered to pay £400 in compensation, and was given a 12-week prison sentence suspended for 18 months, an 18-month supervision order and an indefinite restraining order banning her from contacting Katrice's family, after admitting harassing them via social networking site Facebook.  \n" />
      </a>
      <p>
        
        Donna Wright broke a restraining order to telephone Richard Lee, whose daughter Katrice has not been seen since she disappeared near a British Army base in Germany in 1981.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623606/Bipolar-stalker-harassed-father-toddler-went-missing-1981-having-pretending-daughter-despite-court-order-stay-away.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623606">           0</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mGrHfj| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAD906B00000578-823_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline6}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623387/Security-worker-court-blackmailing-unnamed-celebrity-information-fear-destroy-public.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623387-1DAB5B3800000578-660_154x115.jpg" height="84" width="112" alt="Desmond Fraser, 31, threatened to reveal 'extremely embarrassing' information about the celebrity, who was granted anonymity" />
      </a>
      <p>
        
        Desmond Fraser, 31, threatened to reveal 'extremely embarrassing' information about the star, a court heard. The celebrity, who was granted anonymity, can only be referred to as 'T'.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first gr3ox">
    <a class="http://dailym.ai/1mFKmIb| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623387-1DAB5B3800000578-633_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline7}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623422/Hiding-butchers-Tanzania-Young-girl-seeks-refuge-witch-doctors-want-body-parts-shes-ALBINO.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623422-1DACD09700000578-746_636x382.jpg" height="382" width="636" alt="Albino Tanzanians preview" />
        </a>
      <div >
       <p>
         
         Regarded as the 'tribe of ghosts' or 'the invisibles', albinos have suffered appalling treatment at the hands of their own people who butcher them for their body parts in the disturbingly mistaken belief they will bring them better health and good fortune. Such is the threat against their lives, the Tanzanian government has been opening shelters for albino children to offer them refuge from attacks. Tanzanian President Jakaya Kikwete, who appointed the country's first albino MP in 2008, has also commissioned task forces to investigate the killings.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623422/Hiding-butchers-Tanzania-Young-girl-seeks-refuge-witch-doctors-want-body-parts-shes-ALBINO.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623422">          36</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuPtwv| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623422-1DACD09700000578-746_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline8}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2622830/Millions-eating-halal-food-without-knowing-How-big-brand-shops-restaurants-sell-ritually-slaughtered-meat-dont-label-it.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622830-1DA7176A00000578-553_154x115.jpg" height="84" width="112" alt="Halal" />
      </a>
      <p>
        
        The switch to slaughtering animals in line with Islamic ritual saves money because the end product can be eaten by Muslims and non-Muslims alike.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2622830/Millions-eating-halal-food-without-knowing-How-big-brand-shops-restaurants-sell-ritually-slaughtered-meat-dont-label-it.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622830">       1,768</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Rssl1B| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622830-1DA8931E00000578-46_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline9}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623441/Michael-Gove-writes-ALL-schools-England-warning-watch-signs-students-radicalised-extremists-wake-Trojan-Horse-plot.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623441-1D7128D600000578-845_154x115.jpg" height="84" width="112" alt="Michael Gove has written to all schools and colleges in England warning them to watch out for signs of radicalisation and other forms of child abuse" />
      </a>
      <p>
        
        The Education Secretary said schools and colleges must be aware of any type of child abuse - including radicalisation.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623441/Michael-Gove-writes-ALL-schools-England-warning-watch-signs-students-radicalised-extremists-wake-Trojan-Horse-plot.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623441">         118</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuJzvs| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623441-1D7128D600000578-439_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline10}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623478/Convicted-sex-offender-worked-airport-security-officer-frisking-passengers-faced-fresh-allegations-abusing-teenage-boy.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623478-1DA9FE6F00000578-315_154x115.jpg" height="84" width="112" alt="Convicted: Sex offender James Burns worked as an airport security officer frisking passengers, despite facing fresh allegations of abusing a teenage boy" />
      </a>
      <p>
        
        James Burns, 56, was employed as an aviation security officer at Manchester Airport after passing a criminal record and counter terrorism check.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623478/Convicted-sex-offender-worked-airport-security-officer-frisking-passengers-faced-fresh-allegations-abusing-teenage-boy.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623478">          12</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuQ2Xb| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623478-1DA9FE6F00000578-857_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline11}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623208/Headteacher-relieved-duties-sex-tape-recorded-school-posted-YouTube.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623208-1DA9FB8700000578-758_154x115.jpg" height="84" width="112" alt="Graham Daniels, the head teacher at Bryn Tawe School in Swansea is no longer at the helm of the school while an alleged 'sex tape' recorded in the school is investigated" />
      </a>
      <p>
        
        Governors at Ysgol Gyfun Gymraeg Bryn Tawe in Swansea announced that the deputy headteacher has been put in charge temporarily after the video emerged.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623208/Headteacher-relieved-duties-sex-tape-recorded-school-posted-YouTube.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623208">         136</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru9pj0| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623208-1DAAE77500000578-508_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-large cleared">
    <h2 class="linkro-darkred"><a href="#">{{headline12}}</a>
    </h2>
    <a href="/news/article-2623316/Twitter-troll-42-posted-sickening-messages-praising-killing-teacher-Ann-Maguire-jailed-eight-weeks.html">
        <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623316-1DAD376F00000578-728_308x420.jpg" height="420" width="308" alt="ann" />
    </a>
    <div class="articletext-holder">
      <p>
        
        Robert Riley, from Port Talbot, south Wales, sent the sickening messages after the death of the teacher, inset, from Corpus Christi School, Leeds. The jobless 42-year-old told followers he would have killed 'all the b*****d teachers' at the school.
      </p>
      <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="videos-link" href="/news/article-2623316/Twitter-troll-42-posted-sickening-messages-praising-killing-teacher-Ann-Maguire-jailed-eight-weeks.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuygTW| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623316-1DACD8FE00000578-782_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

    </div>
  </div>


    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline13}}</a>
    </h2>
    <div class="articletext">
        <a href="/femail/article-2623329/An-close-personal-glimpse-inside-Met-Ball-secret-CAMERA-designer-Cynthia-Rowley-hid-purse.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623329-1DAB524700000578-841_636x382.jpg" height="382" width="636" alt="Having a ball: Hayden Pannetiere can be seen laughing as she chats with another guest" />
        </a>
      <div >
       <p>
         
         Fashion designer Cynthia Rowley carried a bejeweled clutch that had a GoPro camera hidden inside, which filmed the festivities through a strategically placed hole. She managed to skillfully keep her purse hidden in pictures taken of her at the event, but she was seen carrying the same bag at the White House Correspondents' Dinner on Saturday.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="Femail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/femail/article-2623329/An-close-personal-glimpse-inside-Met-Ball-secret-CAMERA-designer-Cynthia-Rowley-hid-purse.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623329">         187</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuC1bS| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623329-1DACD85100000578-355_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline14}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623463/Wealthy-heiress-Janet-Brown-murdered-lover-Donald-Graham-hid-body-fraud.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623463-1DAA58AF00000578-613_154x115.jpg" height="84" width="112" alt="Missing: Janet Brown has not been seen since 2005" />
      </a>
      <p>
        
        A wealthy heiress was killed and her body hidden by her lover as part of an audacious fraud that saw him strip her and her elderly parents of all their assets, a court heard today.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first gr3ox">
    <a class="http://dailym.ai/RuMxQw| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623463-1DAD386400000578-190_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline15}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2622995/Squatter-400-000-three-bedroom-house-owned-elderly-woman-WINS-right-ownership-10-years-claiming-squatters-rights.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622995-1DA635EF00000578-285_154x115.jpg" height="84" width="112" alt="Keith Best won the right to the house in Church Road, Ilford, east London after squatting in it for years" />
      </a>
      <p>
        
        Keith Best was told he could remain in the three-bedroom semi-detached house in Ilford despite squatting being made illegal in 2012, due to 'no action by owner'
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2622995/Squatter-400-000-three-bedroom-house-owned-elderly-woman-WINS-right-ownership-10-years-claiming-squatters-rights.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622995">       1,006</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Rthepf| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622995-1DA635EF00000578-572_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline16}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623604/Tory-MP-claimed-expenses-sympathy-cards-sent-families-dead-constituents-new-records-show.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1A965B54000005DC-825_154x115.jpg" height="84" width="112" alt="Tory MP Caroline Dinenage replaced Sir Peter Viggers - who was notorious for his duck island expenses claim - in the safe Conservative seat of Gosport" />
      </a>
      <p>
        
        Caroline Dinenage claimed £3.95 for a pack of three, the Independent Parliamentary Standards Authority revealed. The Gosport MP insisted the claim was fair.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623604/Tory-MP-claimed-expenses-sympathy-cards-sent-families-dead-constituents-new-records-show.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623604">          25</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RvgC2k| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1A965B54000005DC-450_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline17}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623429/Time-ditch-macho-image-allow-women-fight-frontline-Defence-Secretary-Philip-Hammond-says.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622257-1CE2AD1F00000578-840_154x115.jpg" height="84" width="112" alt="Women are not allowed to serve in ground close combat roles, but the ban could now be reviewed earlier than planned" />
      </a>
      <p>
        
        The top Tory said women should be judged on their ability and fitness - not their sex.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623429/Time-ditch-macho-image-allow-women-fight-frontline-Defence-Secretary-Philip-Hammond-says.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623429">         212</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuHCPr| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622257-1CE2AD1F00000578-124_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline18}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623467/Inside-house-filth-animal-charity-worker-kept-pets-conditions-bad-police-officers-forced-wear-GAS-MASKS-rescue-operation.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623467-1DABF2B100000578-523_636x382.jpg" height="382" width="636" alt="Animal cruelty" />
        </a>
      <div >
       <p>
         
         Dorothy Harland, 58 (bottom right), was a founding member of the Emergency Animal Rescue Service (EARS) in Ripon, North Yorkshire. But as she spent her days urging people to take in neglected animals, her own were left suffering in a decrepit house in Harrogate. The conditions were so horrendous that officers who eventually discovered the hovel on December 14 last year could not stay inside for more than a minute without gas masks. RSPCA inspectors found three dogs and four cats trapped between the broken pieces furniture. One of the dogs, Jack, a Saluki (inset left) was found in a rusty cage that was too small to stand in.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623467/Inside-house-filth-animal-charity-worker-kept-pets-conditions-bad-police-officers-forced-wear-GAS-MASKS-rescue-operation.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623467">          43</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mG1MVh| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623467-1DABF2B100000578-523_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline19}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623507/How-rice-wheat-divided-world-Cultural-differences-East-West-FARMING-claims-study.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623507-1DAD880F00000578-616_154x115.jpg" height="84" width="112" alt="Yangzhou, Jiangsu Province, China --- A farmer wades in his flooded rice field in Yangzhou. --- Image by © Ron Watts/CORBIS" />
      </a>
      <p>
        
        A study by the University of Virginia found rice farming methods that make people work together have caused Eastern cultures to become more interdependent.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623507/How-rice-wheat-divided-world-Cultural-differences-East-West-FARMING-claims-study.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623507">           4</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mG6OB4| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623507-1DAD880F00000578-164_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline20}}</a>
    </h2>
    <div class="articletext">
      <a href="/health/article-2623455/Could-POLAR-BEARS-help-cure-obesity-DNA-hold-secret-boosting-metabolism-preventing-heart-disease.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623455-1DAD110B00000578-312_154x115.jpg" height="84" width="112" alt="Polar bears could hold the key to the obesity crisis, new research suggests" />
      </a>
      <p>
        
        Researchers at the University of California and the University of Copenhagen found the animal's DNA is uniquely evolved to cope with a high fat diet.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/health/article-2623455/Could-POLAR-BEARS-help-cure-obesity-DNA-hold-secret-boosting-metabolism-preventing-heart-disease.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623455">          46</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mG4wlq| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623455-1DAD110B00000578-290_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline21}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623321/Gang-baby-faced-murderers-young-14-laughed-joked-trial-named-judge-showing-no-remorse.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623321-1DAB670000000578-753_636x382.jpg" height="382" width="636" alt="Joseph McGill, 14 (left), Reese O'Shaughnessy, 19, (clockwise from top left), Keyfer Dykstra, 14, Corey Hewitt, 14 and Andrew Hewitt, 15, were convicted of killing Sean McHugh (inset) in Anfield, Liverpool" />
        </a>
      <div >
       <p>
         
         Joseph McGill, 14 (left), Reese O'Shaughnessy, 19, (clockwise from top left), Keyfer Dykstra, 14, Corey Hewitt, 14 and Andrew Hewitt, 15, were convicted of killing Sean McHugh (inset) in Anfield, Liverpool. Rival Mr McHugh, 19, was chased down the street and into a launderette by the gang members, before he was attacked with the sword stick, a cane containing a hidden blade, and stabbed in the leg, slashing open a major artery.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623321/Gang-baby-faced-murderers-young-14-laughed-joked-trial-named-judge-showing-no-remorse.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623321">         202</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RufnjX| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623321-1DAB670000000578-753_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline22}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623454/38-000-just-GARAGE-rural-Wales-Detached-outhouse-sale-local-flat-near-prime-angling-spot.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAB1B4300000578-47_154x115.jpg" height="84" width="112" alt="Is this the most expensive garage in Wales?" />
      </a>
      <p>
        
        The simple pebbledash hut measuring 19ft by 10ft is on sale in the picturesque Lledr Valley in north Wales - and has no heating, electricity, running water or windows.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623454/38-000-just-GARAGE-rural-Wales-Detached-outhouse-sale-local-flat-near-prime-angling-spot.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623454">           7</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuNo3H| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623454-1DAD092F00000578-210_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline23}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623532/Mothers-fury-fit-active-five-year-old-son-branded-OVERWEIGHT-school-calculated-BMI-index.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623532-1DAB7D7A00000578-932_156x117.jpg" height="84" width="112" alt="Samantha Timmermans, right, received a letter from her son Jayden's school warning that the five-year-old who loves swimming and riding his bicycle was 'overweight'" />
      </a>
      <p>
        
        A furious mother from Fernwood Notts has hit out after her fit and active five-year-old son was branded 'overweight' in a letter he brought home from school.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623532/Mothers-fury-fit-active-five-year-old-son-branded-OVERWEIGHT-school-calculated-BMI-index.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623532">          29</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mGcuLi| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623532-1DAB7D7A00000578-414_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline24}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623544/Cherie-Blairs-personal-trainer-attacked-racially-abused-bar-husband-lover.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623544-1DAD899B00000578-909_636x382.jpg" height="382" width="636" alt="cherie" />
        </a>
      <div >
       <p>
         
         Steve Agyei (left) was allegedly racially abused by Alexander Hutcheon (right). Mr Hutcheon, 58, is also accused of assaulting his wife Nicola Hutcheon (centre) by poking her in the face with his finger at their luxury home in the west end of Aberdeen. He is also accused of shouting and swearing at her partner Mr Agyei, the former fitness instructor of Cherie Blair (inset), and of making racist remarks in a city bar. Mr Hutcheon, the owner of one of Aberdeen's leading property and mortgaging businesses, went on trial at the city's sheriff court.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first gr3ox">
    <a class="http://dailym.ai/1mGaVgn| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623544-1DAD899B00000578-665_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline25}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623260/Stepfamilies-priced-South-East-afford-larger-homes-total-number-falls-14.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623260-1DAA85E600000578-521_154x115.jpg" height="84" width="112" alt="The proportion of stepfamilies is lowest in London and the South East, where house prices are higher, suggesting larger families are being priced out of some areas" />
      </a>
      <p>
        
        The changing face of Britain’s families was revealed by data showing there were 544,000 families with children living with a stepparent in 2011, down from 631,000 ten years earlier.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623260/Stepfamilies-priced-South-East-afford-larger-homes-total-number-falls-14.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623260">          89</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru2UNi| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623260-1DAA85E600000578-952_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline26}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2622874/Panic-buying-number-homes-sale-falls-Estate-agents-report-average-number-properties-sold-month-highest-level-six-years.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622874-01A3163A0000044D-340_154x115.jpg" height="84" width="112" alt="House prices are ballooning as fewer properties come on to the market, coupled with huge demand which has seen estate agents sell an average of 23 properties in the last three months" />
      </a>
      <p>
        
        The average number of homes sold by an estate agent over the last three months has hit 23, the highest number for six years, as the number of homes coming on to the market falls.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2622874/Panic-buying-number-homes-sale-falls-Estate-agents-report-average-number-properties-sold-month-highest-level-six-years.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622874">         123</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1ioC7fz| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622874-01A3163A0000044D-347_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline27}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623523/Future-wars-fought-cyberspace-stop-soldiers-killed-line-Defence-Secretary-Philip-Hammond-claims.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623523-16770D87000005DC-483_154x115.jpg" height="84" width="112" alt="The Call of Duty video game is hugely popular - but could become reality in the future. While cyber warfare will have nothing to do with video shoot 'em ups, malicious computer viruses are likely to be the new weapon of choice for Western countries that are unwilling to risk their soldiers lives on a real battlefield" />
      </a>
      <p>
        
        Defence Secretary Philip Hammond said internet-based attacks could replace boots on the ground - in the same way tanks replaced horses in the 20th Century.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623523/Future-wars-fought-cyberspace-stop-soldiers-killed-line-Defence-Secretary-Philip-Hammond-claims.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623523">          21</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mG5Gxm| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623523-16770D87000005DC-841_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline28}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623500/The-skin-cancer-app-accurate-DOCTOR-System-uses-high-res-lens-scan-unusual-looking-moles.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623500-1DAD205A00000578-734_154x115.jpg" height="84" width="112" alt="The DermoScreen app works with a dermoscope attachment, pictured. The lens scans unusual looking lesions before highlighting potentially cancerous cells. During tests, the app was accurate in 85% of cases based on visual characteristics - higher than the 50% to 70% average accuracy rate of family doctors" />
      </a>
      <p>
        
        The DermoScreen app, developed in Houston, works with a dermoscope attachment. The lens scans unusual looking lesions and highlights at-risk patients.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623500/The-skin-cancer-app-accurate-DOCTOR-System-uses-high-res-lens-scan-unusual-looking-moles.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623500">           6</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mG5UV0| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623500-1DAD704B00000578-56_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline29}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623388/The-toughest-beef-world-Buffalo-manages-fight-entire-pride-lions-astonished-safari-tourists.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623388-1DAA033A00000578-366_636x382.jpg" height="382" width="636" alt="Gathering: More cars start to approach the fight as it moves onto the dirt road. Another lion tries to grab the buffalo's hind legs" />
        </a>
      <div >
       <p>
         
         Photographer Scott MacLeod captured the moment 11 lions and 12 safari vehicles filled with tourists surrounded the buffalo in Tanzania. The predators were using the vehicles as shade during the hottest part of the day before they launched the attack after spotting a herd in the distance. Despite a relentless attempt by the predators to maul its tail and wrestle it to the ground, the buffalo managed to escape.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623388/The-toughest-beef-world-Buffalo-manages-fight-entire-pride-lions-astonished-safari-tourists.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623388">         151</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuAS4l| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623388-1DABBE9F00000578-409_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline30}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623520/Stuart-Hall-used-annexe-BBC-dressing-room-abuse-young-girls-raped-one-like-rag-doll-trial-told.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623520-1DAD6DF200000578-647_154x115.jpg" height="84" width="112" alt="Hall" />
      </a>
      <p>
        
        A woman, now in her late 40s, wept today as she told a court how Hall, now 84, had sexually abused her at two BBC studios in Manchester - Oxford Road and Piccadilly.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first gr3ox">
    <a class="http://dailym.ai/RuV71I| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623520-1DAD6DF200000578-980_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline31}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623085/Mother-arrested-allegedly-trying-cut-throats-three-children-kitchen-knife.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623085-1DA3047400000578-688_154x115.jpg" height="84" width="112" alt="Police at the scene in Newport, South Wales yesterday after two children and their mother were taken to hospital with suspected knife wounds" />
      </a>
      <p>
        
        The 27-year-old is said to have used a kitchen knife to attack her seven-year-old son and 16-month-old girl in an attack in Newport, South Wales yesterday
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="videos-link" href="/news/article-2623085/Mother-arrested-allegedly-trying-cut-throats-three-children-kitchen-knife.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtCLhw| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623085-1DA3047400000578-86_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline32}}</a>
    </h2>
    <div class="articletext">
      <a href="/health/article-2623437/High-cholesterol-help-CANCER-spread-body-researchers-warn.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623437-1DACE9EF00000578-204_154x115.jpg" height="84" width="112" alt="'Bad' cholesterol can help cancer cells move around the body, new research suggests" />
      </a>
      <p>
        
        Researchers at the University of Sydney say that, in contrast, 'good' cholesterol can make it more difficult for cancer cells to spread around the body.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/health/article-2623437/High-cholesterol-help-CANCER-spread-body-researchers-warn.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623437">          24</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuSgpp| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623437-1DACE9EF00000578-237_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline33}}</a>
    </h2>
    <div class="articletext">
      <a href="/health/article-2623324/Being-depressed-angry-teenager-affect-love-life-25-YEARS-later.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623324-0A0BEBBF000005DC-176_154x115.jpg" height="84" width="112" alt="Depression and anger that people experience as teenagers can taint their love lives even 25 years later" />
      </a>
      <p>
        
        Researchers at the University of Alberta say depression suffered as a teenager clings to people throughout their future relationships.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/health/article-2623324/Being-depressed-angry-teenager-affect-love-life-25-YEARS-later.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623324">          52</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFJtzi| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623324-0A0BEBBF000005DC-998_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline34}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623285/Anger-retired-policeman-85-year-old-mother-dead-hospital-bed-visit.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623285-1DAD8AE100000578-363_636x382.jpg" height="382" width="636" alt="mum" />
        </a>
      <div >
       <p>
         
         Martyn James had to inform nurses his mother Joan (pictured left earlier in her stay at the hospital and, right, with her family) after finding her 'propped up' and 'cold' in her bed at Heartlands Hospital, Birmingham, an inquest has heard. The retired policeman said he had been downstairs having coffee when he popped back up to see his mother, 30 minutes after she had last been checked by a nurse. But when he arrived at her bedside, he noticed she wasn't moving.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623285/Anger-retired-policeman-85-year-old-mother-dead-hospital-bed-visit.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623285">          97</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFkGeR| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623285-1DAD722000000578-21_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline35}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623290/Give-free-meals-Ill-bad-review-TripAdvisor-Anger-blackmailers-using-online-ratings-website-extort-free-rooms-dinners-hotels-restaurants.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623290-1DA9FD3B00000578-445_154x115.jpg" height="84" width="112" alt="Blackmail: Craig Savage and partner Sarah Bird outside their restaurant, Double Barrel Bar and Grill in Rotherham, South Yorkshire. Customers have been threatening to give the restaurant bad reviews online unless they were given free or discounted meals" />
      </a>
      <p>
        
        Fraudsters are telling staff they will post bad comments on the review site if they don't get better service, meals or upgrades.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623290/Give-free-meals-Ill-bad-review-TripAdvisor-Anger-blackmailers-using-online-ratings-website-extort-free-rooms-dinners-hotels-restaurants.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623290">         168</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuchfL| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623290-1DAB338C00000578-547_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline36}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623083/Barclays-axes-19-000-jobs-including-7-000-investment-bankers.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-11B925D3000005DC-181_154x115.jpg" height="84" width="112" alt="Barclays has announced it is to axe 7,000 jobs from its investment banking division by 2016" />
      </a>
      <p>
        
        A total of 7,000 jobs will go in its investment division, including more than 2,000 in the UK, marking the end of an era for the high-stakes casino banking which defined the financial crisis.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623083/Barclays-axes-19-000-jobs-including-7-000-investment-bankers.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623083">         583</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623083/Barclays-axes-19-000-jobs-including-7-000-investment-bankers.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFzmdP| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-11B925D3000005DC-251_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline37}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623330/Is-Inter-Stellar-Assistance-Force-Mysterious-UFO-filmed-blitzing-Taliban-base-Afghanistan.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623330-1DAB765400000578-372_636x382.jpg" height="382" width="636" alt="ufo" />
        </a>
      <div >
       <p>
         
         With Nato forces withdrawing from the badlands of Afghanistan, the country's people need all the help they can get to keep extremists from once again seizing power. But it seems a new intervention has come from an unlikely source... outer space. U.S. Marines captured this incredible footage of what looks like a UFO hovering over a Taliban encampment - then blowing it to kingdom come. The clip was reportedly filmed by U.S. troops fighting in Afghanistan in March.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623330/Is-Inter-Stellar-Assistance-Force-Mysterious-UFO-filmed-blitzing-Taliban-base-Afghanistan.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623330">         712</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623330/Is-Inter-Stellar-Assistance-Force-Mysterious-UFO-filmed-blitzing-Taliban-base-Afghanistan.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ruibxz| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623330-1DAB765400000578-153_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline38}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623186/Tories-exploiting-death-tragic-teacher-Ann-Maguire-headline-grabbing-knife-crackdown-claims-Clegg.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623186-1DAA39C900000578-991_154x115.jpg" height="84" width="112" alt="Nick Clegg defended his knife crackdown veto on his weekly LBC phone in this morning" />
      </a>
      <p>
        
        The Deputy Prime Minister said he would not support mandatory jail sentences for those caught carrying a knife for the second time.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623186/Tories-exploiting-death-tragic-teacher-Ann-Maguire-headline-grabbing-knife-crackdown-claims-Clegg.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623186">         403</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623186/Tories-exploiting-death-tragic-teacher-Ann-Maguire-headline-grabbing-knife-crackdown-claims-Clegg.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtSXPX| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623186-1DAA39C900000578-318_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline39}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623183/Pupils-school-hospitalised-smoking-legal-high-Pandoras-Box-break-time-boasting-Facebook-Lets-high.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623183-1DA9EDD200000578-690_154x115.jpg" height="84" width="112" alt="Three GCSE pupils from a top Roman Catholic school have been taken to hospital after smoking a 'legal high' narcotic during a secret drug taking session at break-time" />
      </a>
      <p>
        
        The two boys and one girl aged 15 and 16 were among six youngsters who took a quantity herbal drugs during a morning break at St Mary's Catholic College in Blackpool, Lancashire.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623183/Pupils-school-hospitalised-smoking-legal-high-Pandoras-Box-break-time-boasting-Facebook-Lets-high.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623183">          16</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtWDBd| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623183-1DAA9C6700000578-447_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline40}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623491/China-considers-building-rail-link-AMERICA-8-000-mile-journey-two-days-involve-going-125-mile-undersea-tunnel-Alaska.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623491-0152F22600001005-491_154x115.jpg" height="84" width="112" alt="Ambitious plans: The 8,000-mile high-speed link would begin in north east China and end up in the US" />
      </a>
      <p>
        
        Travelling at around 217mph, the train would start in the north east of the county and cross parts of Russia, Alaska and Canada before reaching the US.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623491/China-considers-building-rail-link-AMERICA-8-000-mile-journey-two-days-involve-going-125-mile-undersea-tunnel-Alaska.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623491">          25</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mG3BRT| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623491-0152F22600001005-376_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline41}}</a>
    </h2>
    <div class="articletext">
      <a href="/femail/article-2622268/Is-goodbye-Botox-Face-gym-based-16th-century-techniques-claims-smooth-skin-wrinkle-workout.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622268-1DA48A4D00000578-673_154x115.jpg" height="84" width="112" alt="Woman Surrounded by Syringes --- Image by Â© Joerg Steffens/Corbis" />
      </a>
      <p>
        
        This non-invasive finger-led facelift recreates a typical gym workout with a warm-up, interval training and cool down stage.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="Femail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/femail/article-2622268/Is-goodbye-Botox-Face-gym-based-16th-century-techniques-claims-smooth-skin-wrinkle-workout.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622268">          24</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtQtks| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622268-1DA48A4D00000578-675_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline42}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623425/Inventor-comes-redesign-axe-8-000-years-curved-blade-stops-swinging-straight-wood-leg.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623425-1DACDAD900000578-950_636x382.jpg" height="382" width="636" alt="The newly designed Leveraxe, created by retired Finnish man Heikki Karna" />
        </a>
      <div >
       <p>
         
         Heikki Karna, a retired air traffic controller from Finland, came up with the idea of the Leveraxe when clearing trees to build himself a new home in the forest. The design of the axe means it can cut an individual piece of fire wood with one swipe and stops immediately on impact, reducing the risk of injury.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623425/Inventor-comes-redesign-axe-8-000-years-curved-blade-stops-swinging-straight-wood-leg.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623425">          50</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623425/Inventor-comes-redesign-axe-8-000-years-curved-blade-stops-swinging-straight-wood-leg.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuKhJ8| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623425-1DACDAD900000578-950_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline43}}</a>
    </h2>
    <div class="articletext">
      <a href="/health/article-2622560/Woman-wisdom-tooth-extracted-using-HYPNOSIS-deal-pain.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622560-1DA5B2F400000578-304_154x115.jpg" height="84" width="112" alt="Ms Waxkirsh (pictured as the tooth was removed) says she put herself into a trance-like state" />
      </a>
      <p>
        
        Sharon Waxkirsh, a hypnotist who works in London, says that she felt no pain during or after the procedure despite being given no pain relief medication.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/health/article-2622560/Woman-wisdom-tooth-extracted-using-HYPNOSIS-deal-pain.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622560">          76</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/health/article-2622560/Woman-wisdom-tooth-extracted-using-HYPNOSIS-deal-pain.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RrDRdL| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622560-1DA5B2F400000578-55_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline44}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623430/Taking-selfies-just-got-sharper-Super-sensor-adds-digital-camera-style-optical-zoom-gadgets.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623430-1DABB75D00000578-550_154x115.jpg" height="84" width="112" alt="Engineers from Israel designed the dual-lens system to make it small enough to fit in a smartphone. The technology is capable of achieving an optical zoom five times greater than 3x digital zoom and is also used to create depth of field effects that can be altered after the shot has been taken" />
      </a>
      <p>
        
        The Israeli system achieves an optical zoom five times greater than 3x digital zoom and is also used to create depth of field effects that can be edited.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623430/Taking-selfies-just-got-sharper-Super-sensor-adds-digital-camera-style-optical-zoom-gadgets.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623430">           4</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mGcMlf| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623430-1DAD252500000578-333_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline45}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623239/Former-Boko-Haram-negotiator-says-group-plan-exchange-300-kidnapped-schoolgirls-comrades-imprisoned-Nigeria.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/05/article-2620615-1D96060100000578-733_154x115.jpg" height="84" width="112" alt="Warning: A grab taken from a video obtained by French news agency AFP which shows the leader of Islamist group Boko Haram, Abubakar Shekau (centre), vowing to sell hundreds of captured schoolgirls as sex slaves" />
      </a>
      <p>
        
        Shehu Sani, a former negotiator with the militant group says they are using the missing schoolgirls as 'bargaining chips', it has been reported.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623239/Former-Boko-Haram-negotiator-says-group-plan-exchange-300-kidnapped-schoolgirls-comrades-imprisoned-Nigeria.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623239">          65</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623239/Former-Boko-Haram-negotiator-says-group-plan-exchange-300-kidnapped-schoolgirls-comrades-imprisoned-Nigeria.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru0376| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/05/article-2620615-1D96060100000578-271_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline46}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623254/Scotland-Yard-detectives-leading-hunt-Madeleine-McCann-arrive-Portugal-ahead-excavations-town-vanished.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623254-1DAADB1200000578-954_154x115.jpg" height="84" width="112" alt="Police" />
      </a>
      <p>
        
        Specialist Metropolitan Police officers are expected to examine several sites in Praia da Luz after permission to dig was granted by Portuguese authorities.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623254/Scotland-Yard-detectives-leading-hunt-Madeleine-McCann-arrive-Portugal-ahead-excavations-town-vanished.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623254">           6</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623254/Scotland-Yard-detectives-leading-hunt-Madeleine-McCann-arrive-Portugal-ahead-excavations-town-vanished.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru1Nx0| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623254-1DAB299300000578-84_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline47}}</a>
    </h2>
    <div class="articletext">
        <a href="/sciencetech/article-2623514/The-incredible-graphic-reveals-screens-buttons-dials-switches-Sauber-Formula-1-steering-wheel.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623514-1DAD6ACC00000578-904_636x382.jpg" height="382" width="636" alt="Where's the ignition switch? Sauber's 2014 Formula One steering wheel has a huge array of switches, dials and buttons as well as a large screen." />
        </a>
      <div >
       <p>
         
         Drivers of the most advanced cars in the world are expected to master a vast array of screens, dials, buttons and switches to control their car - as well as having to learn to control its unbelievable power. This image shows exactly what Sauber drivers Esteban Gutierrez and Adrian Sutil deal with.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623514/The-incredible-graphic-reveals-screens-buttons-dials-switches-Sauber-Formula-1-steering-wheel.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623514">           9</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mGc6wg| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623514-1DAD6ACC00000578-904_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline48}}</a>
    </h2>
    <div class="articletext">
      <a href="/health/article-2623176/How-boardroom-affects-bedroom-Higher-earners-sex-they-adventurous.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623176-17688711000005DC-787_154x115.jpg" height="84" width="112" alt="Just four per cent of high earners have sex every day - a figure that triples for lower earners" />
      </a>
      <p>
        
        Research by the sex toy company Lovehoney revealed that just four per cent of high earners have sex every day - a figure that triples for low earners.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/health/article-2623176/How-boardroom-affects-bedroom-Higher-earners-sex-they-adventurous.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623176">          43</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mF2jqp| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623176-17688711000005DC-957_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline49}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623265/Do-not-call-racist-party-Farage-demands-poses-black-Asian-Ukip-supporters-ethnic-minority-rally.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623265-1DA6E86E00000578-555_154x115.jpg" height="84" width="112" alt="The Ukip leader said the party was not racist - and paraded a host of ethnic minority supporters as proof" />
      </a>
      <p>
        
        The Ukip leader staged a ‘myth-busting’ event in an attempt to counter a string of damaging stories about racist and sexist comments made by some candidates.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623265/Do-not-call-racist-party-Farage-demands-poses-black-Asian-Ukip-supporters-ethnic-minority-rally.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623265">         455</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623265/Do-not-call-racist-party-Farage-demands-poses-black-Asian-Ukip-supporters-ethnic-minority-rally.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru5SRY| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623265-1DA6E86E00000578-816_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="item channel_teaser_wrapper">
    <div class="teaser femail"
       data-track-module="sm-843^channel_teaser">
    <a href="/femail/index.html" class="cleared wocc">
      <span class="s-c">
        <span class="first">Femail</span>
          <span>Femail</span>
          <span>Fashion Finder</span>
        <span class="last">More...</span>
      </span>
      <span class="t-a">
        <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622554-1DA58E8B00000578-682_308x185.jpg" alt="World War II" width="308" height="185" />
        <span>World War II as you've NEVER seen it before! Light-hearted photos of nude British and Allied...</span>
      </span>
    </a>
  </div>

  </div>

          <div class="item channel_teaser_wrapper">
    <div class="teaser travel"
       data-track-module="sm-842^channel_teaser">
    <a href="/travel/index.html" class="cleared wocc">
      <span class="s-c">
        <span class="first">Travel</span>
          <span>Travel</span>
          <span>Destinations</span>
        <span class="last">More...</span>
      </span>
      <span class="t-a">
        <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623220-1DAAD76A00000578-191_308x185.jpg" alt="PIC FROM CATERS NEWS - (PICTURED: The restaurant) - DEEP sea diners enjoy a meal surrounded by sharks at the worlds only underwater restaurant. Ithaa in the Maldives sits three metres below the surface of the Indian Ocean in a vibrant coral garden. The all-glass structure - which consists of three five-metre wide, 125mm thick glass arches - allows diners to scoff caviar as sharks and sting-rays swim by. SEE CATERS COPY." width="308" height="185" />
        <span>Dine with sharks, stingrays and turtles! Inside the world's first glass underwater restaurant,...</span>
      </span>
    </a>
  </div>

  </div>

          <div class="item channel_teaser_wrapper">
    <div class="teaser sciencetech"
       data-track-module="sm-844^channel_teaser">
    <a href="/sciencetech/index.html" class="cleared wocc">
      <span class="s-c">
        <span class="first">Science</span>
          <span>Science</span>
          <span>Pictures</span>
        <span class="last">More...</span>
      </span>
      <span class="t-a">
        <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623500-1DAD704B00000578-504_308x185.jpg" alt="Skin cancer app" width="308" height="185" />
        <span>The app that detects skin cancer - and could be more accurate than a DOCTOR: System uses...</span>
      </span>
    </a>
  </div>

  </div>

          <div class="item channel_teaser_wrapper">
    <div class="teaser sport"
       data-track-module="sm-841^channel_teaser">
    <a href="/sport/index.html" class="cleared wocc">
      <span class="s-c">
        <span class="first">Sport</span>
          <span>Football</span>
          <span>World Cup</span>
        <span class="last">More...</span>
      </span>
      <span class="t-a">
        <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/1399555172483_Large_Preview_galleryImage_Onderwerp_Subject_Holland.JPG" alt="" width="308" height="185" />
        <span>Don't mess with Louis: Incoming Manchester United boss Van Gaal shows Dutch players who's in...</span>
      </span>
    </a>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="item channel_mpu_wrapper">
    <div class="mpu adHolder" id="ad-abs-0">
    <script type="text/javascript">adverts.reg('ad-abs-0');</script>
  </div>

  </div>

          <div class="home item image_strapline_slant_wocc_module">
    <div class="image-strapline image-strapline-small" id="p-599">
    <div class="link-wocc linkro-bocc">
      <a href="/news/article-2623242/Sounds-completely-potty-A-fire-engine-FOUR-firefighters-help-free-toddler-jammed-head-neck-training-potty-mother-kitchen.html">
        <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623316-1DA9E32900000578-17_308x385.jpg" height="385" width="308" alt="Completely potty: Layton Kennington, 18 months, had to be freed by a team of four firefighters after he got his head stuck in his training potty" title="Completely potty: Layton Kennington, 18 months, had to be freed by a team of four firefighters after he got his head stuck in his training potty"/>
        <span class="link-text">
          <span class="slant-small-t">&nbsp;</span>
          <span class="inner-text xocc">{{headline50}}</span>
          <span class="slant-small-b">&nbsp;</span>
        </span>
        <span class="tl">&nbsp;</span>
        <span class="tr">&nbsp;</span>
        <span class="bl">&nbsp;</span>
        <span class="br">&nbsp;</span>
      </a>
    </div>
  </div>
  </div>
  <script type="text/javascript">
    DM.has('p-599', 'comScore', {
      mo_mod_id: '1035911',
      mo_mod_pos: 'p-599'
    });
  </script>

    </div>
  </div>

  </div>

        <div class="beta">
        <div class="item beta_search_wrapper">
    <a name="search"></a>
    <form id="p-602-bing" name="searchForm" action="/home/search.html" method="get">
    <div class="bing cnr5">
      <fieldset class="cleared">
        <legend class="usability">Bing</legend>
        <div class="bow cleared">
          <span class="ctnr-l">
            <span class="nowrap"><input id="p-602-bing-site" name="sel" value="site" type="radio" class="ie-radio" checked="checked" /><label for="p-602-bing-site">Site</label></span>
            <span class="nowrap"><input id="p-602-bing-web" name="sel" value="web" type="radio" class="ie-radio" /><label for="p-602-bing-web">Web</label></span>
          </span>
          <span class="ctnr-r">
            <label for="p-602-searchPhrase" class="usability">Enter search term:</label>
            <input id="p-602-searchPhrase" class="text-input" name="searchPhrase" type="text"><button type="submit"><span class="usability">Search</span></button>
          </span>
        </div>
        <span class="bing-logo"></span>
      </fieldset>
      <span class="tl"></span>
      <span class="tr"></span>
      <span class="bl"></span>
      <span class="br"></span>
    </div>
    </form>
  <script type="text/javascript">
    DM.has('p-602-bing', 'bingSearchBox');
  </script>
  </div>

        <div class="home item html_snippet_module">
    <ul class="puff-follow">
      <li class="facebook">
          <a alt="Facebook">
              <b>Like</b>
              <span>DailyMail</span>
          </a>    
      </li>
      <li class="twitter">
          <a alt="Twitter">
              <b>Follow</b>
              <span>MailOnline</span>
          </a>
      </li>
      <li class="pinterest">
          <a alt="Pinterest">
              <b>Follow</b>
              <span>DailyMail</span>
          </a>
      </li>
      <li class="gplus">
          <a alt="GooglePlus One">
              <b>+1</b>
              <span>DailyMail</span>
          </a>
      </li> 
  </ul>
  <script>
          PuffShare.init({});
  </script>
  </div>

        <div class="femail item">
    <div class="puff cleared" id="p-604"
       data-track-module="llg-1000113^puff">
    
    <span class="tl">&nbsp;</span>
    <span class="tr">&nbsp;</span>
    <h3 class="wocc">DON'T MISS</h3>
    <ul class="link-bogr2 linkro-wocc">
      <li>
        <a href="/tvshowbiz/article-2623386/Lenny-Henry-shows-results-drastic-three-stone-weight-loss-steps-London-looking-dapper.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623386-1DAB99BD00000578-777_154x115.jpg" height="115" width="154" alt="Slim: Lenny Henry certainly looked slim and dapper while out and about in London on Tuesday" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Lenny Henry shows the results of drastic three- stone weight loss as he steps out in London looking dapper
            </strong>
            Lost weight to combat effects of diabetes
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623353/My-abs-look-little-different-Jessica-Ennis-Hill-compares-baby-bump-famous-Olympic-six-pack.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623353-1DAB46AC00000578-703_154x115.jpg" height="115" width="154" alt="Jessica Ennis wins gold in the Heptathlon.\nOlympic Games. Olympic stadium," />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'My abs look a little different now': Jessica Ennis-Hill compares her baby bump to her famous Olympic six- pack
            </strong>
            She's really blooming
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623465/Cristiano-Ronaldo-adorable-son-coordinate-white-hats-shades-enjoy-day-Madrid-Open.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623465-1DAD553900000578-497_154x115.jpg" height="115" width="154" alt="We're matching daddy! Cristiano Ronaldo and his adorable son coordinate white hats and shades as they enjoy day out at the Madrid Open" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            We're matching daddy! Cristiano Ronaldo and his adorable son coordinate white hats and shades as they enjoy day out at the Madrid Open
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623622/Hes-Prince-Charming-Angelina-Jolie-accompanied-Brad-Pitt-private-reception-Disney-movie-Maleficent.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623622-1DADB1B000000578-102_154x115.jpg" height="115" width="154" alt="Brad Pitt and Angelina Jolie at provate reception for Maleficent" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            He's her Prince Charming: Angelina Jolie is accompanied by Brad Pitt at private reception for Disney movie Maleficent
            </strong>
            At Kensington Palace
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623624/Angelina-Jolie-makes-chilling-entrance-christening-wasnt-invited-Maleficent-clip.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623624-1DADC0EA00000578-479_154x115.jpg" height="115" width="154" alt="'What an awkward situation': Angelina Jolie makes a chilling entrance to christening she wasn't invited to in first Maleficent clip" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'What an awkward situation': Angelina Jolie makes a chilling entrance to christening she wasn't invited to in first Maleficent clip
            </strong>
            Intriguing glimpse
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623533/Mario-Falcone-gushes-amazing-new-girlfriend-met-Dubai-inspired-settle-down.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623533-1DACCF2C00000578-791_154x115.jpg" height="115" width="154" alt="'I can't wait to have kids': TOWIE's Mario Falcone gushes about 'amazing' new girlfriend he met in Dubai after being inspired to settle down" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'I can't wait to have kids': TOWIE's Mario Falcone gushes about 'amazing' new girlfriend he met in Dubai after being inspired to settle down
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2623525/The-Duchess-Cornwall-puts-brave-face-meets-wounded-airmen-public-appearance-funeral-brother-Mark-Shand.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623525-1DAD302E00000578-564_154x115.jpg" height="115" width="154" alt="Camilla" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Duchess of Cornwall puts on a brave face as she meets wounded airmen during her first public appearance since the funeral of her brother, Mark Shand
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623322/Denise-Welch-shows-incredible-bikini-body-navy-two-piece-relaxing-pool-Tenerife.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623322-1DAB357F00000578-704_154x115.jpg" height="115" width="154" alt="She's the ultimate loser: Denise Welch shows off incredible bikini body and weight loss in navy two-piece relaxing pool-side in Tenerife" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            She's the ultimate loser: Denise Welch shows off incredible bikini body and weight loss in navy two-piece relaxing pool-side in Tenerife
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623390/Sam-Faiers-shows-slender-frame-models-unique-Surf-Bubble-Dress-new-campaign.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DABA21E00000578-121_154x115.jpg" height="115" width="154" alt="Sam Faiers shows off her slender frame as she models unique Surf Bubble Dress for new campaign" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            She scrubs up well! Sam Faiers shows off her slender frame as she models unique Surf Bubble Dress for new campaign
            </strong>
            Bubbly Essex girl!
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623245/Lily-Allen-shares-snap-drip-saying-down.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623245-1DAA7B5E00000578-995_154x115.jpg" height="115" width="154" alt="Lily Allens sparked concern from her fans on Twitter after she posted a snap of herself in hospital" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'Sheezus in Shospital': Lily Allen shares snap of herself ill on a drip as she reveals that she 'can't keep anything down'... after a hectic week of partying
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623274/Kieran-Hayler-spotted-time-sexual-affair-pregnant-wife-Katie-Prices-best-friend-revealed-Twitter-former-glamour-model.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623274-1DAAF31D00000578-267_154x115.jpg" height="115" width="154" alt="PICTURED: Kieran Hayler spotted for the first time since 'sexual affair' with pregnant wife Katie Price's best friend was revealed on Twitter by the former glamour model" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            PICTURED: Kieran Hayler spotted after pregnant wife Katie Price revealed on Twitter his 'sexual affair' with HER best friend
            </strong>
            Looked sheepish
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623559/Jennifer-Lawrence-reveals-having-space-keeps-relationship-strong-poses-stunning-shoot.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623559-1DAD718000000578-488_154x115.jpg" height="115" width="154" alt="'We mutually ignore each other': Jennifer Lawrence reveals how having space keeps her relationship strong as she poses for stunning shoot" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'We mutually ignore each other': Jennifer Lawrence reveals how having space keeps her relationship strong as she poses for stunning shoot
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623540/Connor-Cruise-shows-effects-partying-lifestyle-hits-beach-shirtless-sporting-fuller-physique.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623540-1DADBB8200000578-295_154x115.jpg" height="115" width="154" alt="Connor" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Connor Cruise shows effects of his partying lifestyle as he hits the beach shirtless sporting a fuller physique in Mexico
            </strong>
            Lost his toned chest
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623428/Lucy-Watson-wows-elegant-midnight-blue-lace-pencil-dress-launch-new-fashion-range.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DABCBAD00000578-585_154x115.jpg" height="115" width="154" alt="Lucy Watson for Lipsy VIP" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            A royally good look! Lucy Watson wows in elegant midnight blue lace pencil dress at launch of new fashion range
            </strong>
            Every inch the socialite
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623550/Whitney-Houstons-estate-suing-late-singers-belongings-inside-former-New-Jersey-home.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623550-1DAD995700000578-734_154x115.jpg" height="115" width="154" alt="Whitney Houston's estate suing to get the late singer's belongings from inside her former New Jersey home" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Whitney Houston's estate suing to get the late singer's belongings from inside her former New Jersey mansion
            </strong>
            Claims housesitters changed the locks
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623413/Applause-fashion-leader-Coleen-Rooney-wins-marks-nude-ensemble-Boodles-Ladies-Day-races.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623413-1DAD1D4D00000578-89_154x115.jpg" height="115" width="154" alt="Coleen Rooney" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Coleen Rooney wins top marks for her ladylike nude dress and patent heels as she and husband Wayne enjoy a day at the races
            </strong>
            Boodles Ladies Day
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623471/Paula-Patton-opens-Robin-Thicke-time-split-poses-topless-sizzling-shoot.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623471-1DAD000A00000578-419_154x115.jpg" height="115" width="154" alt="'There is a deep love there': Paula Patton opens up about Robin Thicke for first time since split as she poses topless in sizzling shoot" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'There is a deep love there': Paula Patton opens up about Robin Thicke for first time since split as she poses topless for sizzling shoot
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623593/Claire-Danes-leaves-baby-home-enjoy-date-husband-Hugh-Dancy-book-launch-party.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623593-1DAD63B600000578-674_154x115.jpg" height="115" width="154" alt="Mommy's night off! Claire Danes leaves baby at home to enjoy date with husband Hugh Dancy at book launch party" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Mommy's night off! Claire Danes leaves baby at home to enjoy date with husband Hugh Dancy at book party
            </strong>
            Films Homeland's fourth season this summer
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623475/Zac-Efron-sells-Hollywood-Hills-party-pad-2-75m-splashes-4m-five-bedroom-home-nearby.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/03/17/article-2582941-1C5F1FEC00000578-929_154x115.jpg" height="115" width="154" alt="Making a fresh start! Clean and sober Zac Efron is selling his Hollywood Hills party pad for $2.85 million" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            He won't be a Bad Neighbor! Zac Efron sells Hollywood Hills party pad for $2.75m and splashes $4m on five bedroom home nearby
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623462/Rumer-Willis-shows-derriere-long-legs-sheer-leotard-red-stilettos-Tyler-Shields-photoshoot.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623462-1DAD375300000578-886_154x115.jpg" height="115" width="154" alt="A racy Rumer! Willis shows off her derriere and long legs in sheer leotard and red stilettos for Tyler Shields photoshoot" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Racy Rumer Willis shows off her derriere and long legs in sheer leotard and red stilettos for Tyler Shields photoshoot
            </strong>
            Flaunting with reason
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623594/Hilaria-Baldwin-strikes-latest-yoga-pose-day-ten-pin-contortion.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623594-1DAD5DC000000578-201_154x115.jpg" height="115" width="154" alt="Now we¿re really bowled over! Hilaria Baldwin ¿strikes¿ her latest yoga pose of the day" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Now we're really bowled over! Hilaria Baldwin 'strikes' her latest yoga pose of the day with ten-pin contortion
            </strong>
            Does she ever stop?<br>
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623268/Jodi-Albert-looks-royally-pleased-dazzles-aqua-Prince-Harry-charitys-10th-anniversary-summer-ball.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623268-1DAADEDE00000578-42_154x115.jpg" height="115" width="154" alt="Jodi Albert looks royally pleased as she dazzles in aqua with Prince Harry at his charity's 10th anniversary summer ball" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Jodi Albert looks royally pleased as she dazzles in aqua next to husband Kian Egan at Prince Harry's charity summer ball
            </strong>
            Made it a 'Girl Thing'
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2623224/Georgia-Salpa-proves-FHMs-fifth-sexiest-woman-world-new-lingerie-shoot.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623224-1DAADA1600000578-367_154x115.jpg" height="115" width="154" alt="georgia salpa" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Georgia Salpa replaces Jessica Wright as face of lingerie brand
            </strong>
            Irish model cements place as one of world's sexiest women in sizzling photo shoot
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623538/Sandra-Bullock-dons-leather-night-pals-Chelsea-Handler-Chris-Evans.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623538-1DAD6BFE00000578-231_154x115.jpg" height="115" width="154" alt="With friends like these, who needs a TV? Sandra Bullock dons leather for night out with pals Chelsea Handler and Chris Evans" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            With friends like these, who needs a TV? Sandra Bullock dons leather for night out with pals Chelsea Handler and Chris Evans
            </strong>
            At Cecconi's
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2623452/Perfect-woman-doesnt-exist-mix-five-celebrities-Can-guess-who.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623452-1DAD1CB300000578-654_154x115.jpg" height="115" width="154" alt="Ideal female has Kate Middleton's hair, framing her shapely face, while her full lips belong to Nicole Scherzinger" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Is this the 'perfect face'? We want Kim Kardashian's almond eyes and the Duchess of Cambridge's glossy hair, says new survey - but who else in in the mix...
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623487/Can-I-eat-David-Beckham-looks-exhausted-poses-fans-outside-Miami-restaurant-heading-dinner.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623487-1DAB2B4100000578-968_154x115.jpg" height="115" width="154" alt="David Beckham managed a smile as he posed with the owners of the restaurant in Miami where he was joined by his wife's former manager" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Can I go eat now? David Beckham looks exhausted as he poses with fans outside Miami restaurant before heading for dinner
            </strong>
            Worn and weary
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2623479/High-street-goes-high-end-Exclusive-look-second-M-S-Best-British-collection.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623479-1DAD393F00000578-954_154x115.jpg" height="115" width="154" alt="mands" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            High street goes high end: Exclusive look at second M&amp;S Best of British collection
            </strong>
            Summer collection filled with classic tailoring and modern formal wear
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623483/Halle-Berry-shares-steamy-shower-scene-star-Goran-Visnjic-extended-trailer-sci-fi-series-Extant.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623483-1DABAAF900000578-451_154x115.jpg" height="115" width="154" alt="Halle Berry shares steamy shower scene with co-star Goran Visnjic in extended trailer for sci-fi series Extant" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Halle Berry shares steamy shower scene with co-star Goran Visnjic in extended trailer for sci-fi series Extant
            </strong>
            Scorching stuff
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623300/Not-exactly-shoes-Dancing-Strictly-star-Abbey-Clancy-shops-swimwear-Chelsea-perspex-heels-ripped-jeans.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623300-1DAAFCD100000578-68_154x115.jpg" height="115" width="154" alt="Abbey Clancy" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Not exactly shoes for Dancing: Strictly star Abbey Clancy shops for swimwear in Chelsea in perspex heels and ripped jeans
            </strong>
            Going on another holiday
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623453/Jasmin-Walia-resist-sharing-steamy-selfie-plunging-white-cut-swimsuit.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623453-1DAAE9E300000578-381_154x115.jpg" height="115" width="154" alt="Sexy selfie: Having got a new bathing costume, TOWIE's Yasmin Walia couldn't wait to show it off on Twitter" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Watch your tan-line! Jasmin Walia can't resist sharing a steamy selfie in plunging white cut-out swimsuit
            </strong>
            Towie star justifiably proud of her bikini body
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2623431/Sophie-goes-commando-The-Countess-Wessex-chic-camouflage-visits-5th-Rifles-ahead-deployment-Afghanistan-month.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623431-1DACCC0900000578-632_154x115.jpg" height="115" width="154" alt="Sophie Wessex" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Sophie goes commando! Countess of Wessex is chic in camouflage as she visits the 5th Rifles ahead of deployment to Afghanistan next month
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623405/Keeping-hold-man-Carol-McGiffin-54-stays-close-31-year-old-toyboy-fiance.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623405-1DABFC0D00000578-243_154x115.jpg" height="115" width="154" alt="Keeping hold of her man: Carol McGiffin, 54, stays close to her 31-year-old toyboy fiance" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Keeping hold of her man: Carol McGiffin, 54, stays close to her toyboy fiance Mark Cassidy, 31, during romantic day out
            </strong>
            Mind the age gap
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623293/Alanis-Morissette-shows-lean-physique-polka-dot-bikini-enjoys-relaxing-vacation-family-friends.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAAF3FA00000578-20_154x115.jpg" height="115" width="154" alt="Alanis Morissette  shows off her lean physique in polka dot bikini as she enjoys relaxing vacation with family and friends" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Alanis Morissette shows off her lean physique in polka dot bikini as she enjoys relaxing vacation with family and friends
            </strong>
            In Hawaii
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2623270/Get-supermodel-look-Elle-Macpherson-launches-beauty-tools-range-promises-help-look-fabulous-50-just-like-her.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623270-1DACFE4700000578-411_154x115.jpg" height="115" width="154" alt="elle m" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            I'll have what she's having: Elle Macpherson launches supplements and beauty tools range she says will help you look fabulous at 50... just like her
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623357/Sorry-I-didnt-bow-I-asked-meet-Justin-Bieber-continues-feud-Seth-Rogen-claiming-shy.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAB68B500000578-647_154x115.jpg" height="115" width="154" alt="Justin &amp; Seth" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'Sorry I didn't bow down when I asked to meet you!' Justin Bieber continues feud with Seth Rogen claiming he was shy
            </strong>
            'love ur movies'
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623414/Demi-Lovato-rocks-skintight-leather-Buenos-Aires-concert-visit-backstage-twin-Avril-Lavigne.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623414-1DAD1E2000000578-61_154x115.jpg" height="115" width="154" alt="Demi Lovato rocks out in skintight leather during Buenos Aires concert after visit backstage from her 'twin' Avril Lavigne" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Demi Lovato rocks out in skintight leather during Buenos Aires concert after visit backstage from her 'twin' Avril Lavigne
            </strong>
            On Neon Lights tour<br>
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623464/Miranda-Kerr-looks-stunning-Michael-Kors-flagship-opening-Beijing-just-hours-jetting-Sydney.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623464-1DAD071A00000578-983_154x115.jpg" height="115" width="154" alt="Miranda Kerr looks immaculate as she poses with designer Michael Kors in Beijing just hours after jetting out of Sydney" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            No jet lag here! Miranda Kerr is glowing and gorgeous at Michael Kors flagship opening in Beijing just hours after jetting out of Sydney
            </strong>
            Doll-like as ever
          </span>
        </a>
      </li>
      <li>
        <a href="/news/article-2623338/Ron-Goldmans-sister-time-ran-OJ-car.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623338-1DACDAC900000578-34_154x115.jpg" height="115" width="154" alt="Kim Goldman has revealed that she had the opportunity to kill OJ Simpson a year after he was acquitted of her brother Ron Goldman's murder" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'I could have killed OJ': Ron Goldman's sister reveals how she almost mowed Simpson down with her car a year after he was found not guilty of murder
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623562/Dean-McDermott-wins-points-taking-Tori-Spelling-sushi-dinner-presenting-gift-celebrate-8-years-marriage.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623562-1DAD730700000578-354_154x115.jpg" height="115" width="154" alt="Happy Anniversary! Dean McDermott wins points by taking Tori Spelling to sushi dinner and presenting her with gift to celebrate 8 years of marriage" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Happy Anniversary! Dean McDermott wins points by taking Tori Spelling to sushi dinner and presenting her with gift to celebrate 8 years of marriage
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623315/Kardashians-backlash-Hamptons-locals-intensifies-Kourtney-Khloe-search-mansion-film-spin-show.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAB939100000578-446_154x115.jpg" height="115" width="154" alt="Kardashian" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Kardashians NOT welcome! Backlash from Hamptons locals intensifies as Kourtney &amp; Khloé 'search for a mansion to film their spin-off show'
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623443/Pregnant-Tina-OBrien-shows-growing-baby-bump-cute-new-selfie.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623443-1DAD4E8A00000578-393_154x115.jpg" height="115" width="154" alt="¿Allo bebby¿: Pregnant Tina O¿Brien shows off her growing baby bump in cute new selfie" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'Allo bebby': Pregnant Tina O'Brien shows off her growing baby bump in cute new selfie
            </strong>
            Corrie actress has daughter with ex-co-star Ryan Thomas
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623112/Nicola-Roberts-highlights-stunning-red-hair-green-silk-gown-Gabrielles-Gala.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623112-1DA9E45500000578-810_154x115.jpg" height="115" width="154" alt="Nicola Roberts stunned in a flowing sage gown as she attended Gabrielle's Gala fundraiser." />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Aloud to break the rules! Nicola Roberts highlights her stunning red hair with green silk gown at Gabrielle's Gala
            </strong>
            Red and green should never be seen... or not
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623411/Full-trailer-Dawn-Of-The-Planet-Of-The-Apes-shows-Gary-Oldman-watching-war-erupt-man-versus-ape.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623411-1DAD160C00000578-369_154x115.jpg" height="115" width="154" alt="Apes" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Full trailer for Dawn Of The Planet Of The Apes shows Gary Oldman watching war erupt between man and ape
            </strong>
            Explorers come face to face with monkeys
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623383/Jennifer-Love-Hewitt-reveals-slimline-post-baby-body-gets-workout-stroll-little-Autumn.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623383-1DABA22000000578-839_154x115.jpg" height="115" width="154" alt="Jennifer Love Hewitt reveals her slimline post-baby body as she gets in a workout on a stroll with little Autumn" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Jennifer Love Hewitt reveals her slimline post-baby body as she gets in a workout on a stroll with little Autumn
            </strong>
            Welcomed first child into the world in November
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623558/90210-star-Jason-Priestlye-sells-2-million-Toluca-Lake-home-140-000-loss.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623558-1DAD4F4700000578-628_154x115.jpg" height="115" width="154" alt="Isn't that the Peach Pitts! 90210 star Jason Priestly sells his $2 million Toluca Lake home for a $140,000 loss" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Isn't that the Peach Pitts! 90210 star Jason Priestley sells his $2m Toluca Lake home for a $140,000 loss
            </strong>
            The house spent three years on the market
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623120/Here-Lady-Victoria-Hervey-flaunts-flesh-sideboob-racy-sheer-dress-Gabrielles-Gala-event.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623120-1DA9C83A00000578-796_154x115.jpg" height="115" width="154" alt="Standing out: Lady Victoria Hervey showed off plenty of sideboob at the Gabrielle's Gala event in London on Wednesday night" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Here we go again! Lady Victoria Hervey showcases sideboob and plenty of leg in racy sheer dress at Gabrielle's Gala event
            </strong>
            She's got some front
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623412/Alex-Gerrard-brightens-bleary-Liverpool-vibrant-technicolour-t-shirt.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623412-1DABF41C00000578-376_154x115.jpg" height="115" width="154" alt="A little ray of sunshine: Alex Gerrard brightens up a bleary Liverpool in vibrant technicolour t-shirt and eye-catching red trainers" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            A little ray of sunshine: Alex Gerrard brightens up a bleary Liverpool in vibrant technicolour t-shirt and eye-catching red trainers
            </strong>
            Fighting-fit WAG
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623226/Wedding-blues-Kim-Kardashian-Kanye-West-married-prenup-hashed-out.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623226-1DAACE0900000578-671_154x115.jpg" height="115" width="154" alt="Kanye and Kim" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Wedding blues: Kim Kardashian and Kanye West 'can't get married because their prenup is still being hashed out'
            </strong>
            Want to wed just outside Paris this month
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623042/Kim-Kardashian-continues-mix-elite-circles-joins-Barack-Obama-USC-Shoah-Foundation-event.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623042-1DAABEE300000578-795_154x115.jpg" height="115" width="154" alt="Friends in high places! Kim Kardashian found herself in the elite company of President Barack Obama as she showed her support for survivors of the Armenian genocide at the USC Shoah Foundation 20th Anniversary Ambassadors For Humanity Gala in LA on Wednesday night" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            It's not your wedding day yet! Kim Kardashian wows in cream skirt with dramatic train at USC Shoah Foundation event
            </strong>
            In bridal mode
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623070/Khloes-beau-French-Montana-cuddles-Kris-Jenner-Kim-leaves-guest-list-wedding-Kanye-West.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623070-1DA9629000000578-858_154x115.jpg" height="115" width="154" alt="Kris" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Getting in with the mother-in-law! Khloe's beau French Montana cuddles up to Kris Jenner after Kim leaves him off guest list for her wedding to Kanye West
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622849/Katy-Perry-dresses-cat-Egyptian-kicks-Prismatic-World-Tour-Belfast.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622849-1DAAB73500000578-602_154x115.jpg" height="115" width="154" alt="Katy Perry dazzles in multiple Egyptian themed outfits in Belfast on the first night of her Prismatic World Tour" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Cleopatra coming at ya! Katy Perry wears NINE Egyptian themed outfits in Belfast on the first night of her Prismatic World Tour
            </strong>
            Walk like an Egyptian
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623075/Cara-Delevingne-Joan-Smalls-look-picture-perfect-arrive-party-showing-taut-torsos.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623075-1DA9965500000578-578_154x115.jpg" height="115" width="154" alt="They're model party-goers: Cara Delevingne and Joan Smalls look picture perfect as they both arrive at party showing off taut torsos" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            They're model party-goers: Cara Delevingne and Joan Smalls look picture perfect as they both arrive at party showing off taut torsos
            </strong>
            At Boom Boom Room
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623336/Jet-setter-Kylie-Minogue-leaves-Italy-chic-trench-coat-sexy-performance-The-Voice.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623336-1DAB3CE400000578-565_154x115.jpg" height="115" width="154" alt="Jet-setter Kylie Minogue leaves Italy in chic trench coat after sexy performance on The Voice" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            She's flying around! Jet-setter Kylie Minogue leaves Italy in chic trench coat after sexy performance on The Voice
            </strong>
            She's a shady lady
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622821/Harry-Styles-flips-hair-Rio-swimming-pool-revealing-new-leaf-tattoos-hip.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622821-1DA9EE5F00000578-26_154x115.jpg" height="115" width="154" alt="HARRY STYLES" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Because he's worth it! Harry Styles flips his hair back in Rio swimming pool while revealing the new leaf tattoos on his hip
            </strong>
            How many now, Harry?
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623385/Liv-Tyler-faces-brisk-spring-weather-billowy-trench-coat-NY-school-run-son-Milo.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623385-1DAB9B2F00000578-110_154x115.jpg" height="115" width="154" alt="Wind beneath her sails! Liv Tyler faces the brisk spring weather in billowy trench coat on NY school run with son Milo" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Wind beneath her sails! Liv Tyler faces the brisk spring weather in billowy trench coat on NY school run with son Milo
            </strong>
            Liv's favourite wrap
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623142/She-favourites-Pregnant-Holly-Willoughby-looks-radiant-leaves-Celebrity-Juice-studios-wearing-skinny-jeans-week-row.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623142-1DA9E91A00000578-698_154x115.jpg" height="115" width="154" alt="Holly Willoughby leaving Riverside Studios after filming Celebrity Juice on May 7, 2014 in London, England" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            She's found her favourites: Pregnant Holly Willoughby looks radiant as she leaves Celebrity Juice wearing the same skinny jeans for a third week in a row
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623150/Chloe-Green-arrives-charity-fundraising-event-bondage-inspired-leather-corset-dress-net-skirt.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623150-1DA9DC8B00000578-385_154x115.jpg" height="115" width="154" alt="That's a bit raunchy: Chloe Green arrives at charity fundraising event in bondage-inspired leather corset dress with net skirt" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            That's a bit raunchy: Chloe Green arrives at charity fundraising event in bondage-inspired leather corset dress with net skirt
            </strong>
            Putting on a show
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623000/Miley-Cyrus-displays-long-legs-tiny-denim-shorts-attends-gig-Londons-100-Club-rare-night-Bangerz-tour.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623000-1DA8E98300000578-454_154x115.jpg" height="115" width="154" alt="Miley Cyrus displays her long legs in tiny denim shorts as she attends gig at London's 100 Club on rare night off from Bangerz tour" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Miley Cyrus displays her long legs in tiny denim shorts as she attends gig at London's 100 Club on rare night off from Bangerz tour
            </strong>
            American Hi-Fi gig
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2623502/Im-pawning-huge-designer-bag-jewellery-collection-fund-underwear-business-Former-model-makes-assets-start-new-lingerie-venture.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623502-1DA3047D00000578-332_156x117.jpg" height="115" width="154" alt="Cathy hopes to raise funds for her new lingerie company by pawning her collection of designer goods" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'I'm pawning my huge designer bag and jewellery to fund my underwear business': Former model sells off her assets to kickstart new lingerie venture
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623180/Jessie-J-dons-unflattering-silk-pyjama-style-ensemble-charity-gala-offered-porridge-dressing-room.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA9F78D00000578-816_154x115.jpg" height="115" width="154" alt="Jessie. J" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Jessie J dons unflattering silk pyjama-style outfit to charity gala... and is offered porridge in her dressing room
            </strong>
            She's a bed head!
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623326/Love-air-Amanda-Seyfried-kisses-boyfriend-Justin-Long.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623326-1DAA464A00000578-991_154x115.jpg" height="115" width="154" alt="Sign of love: Amanda Seyfried kisses her boyfriend, fellow actor Justin Long go shopping at the farmers market in Union Square, Manhattan" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Love-lace is in the air: Amanda Seyfried takes a break from grocery shopping to kiss boyfriend Justin Long
            </strong>
            At the Farmers Market in Manhattan
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623278/Partner-look-Kaley-Cuoco-husband-Ryan-Sweeting-honeymoon-phase-dress-alike-lunch-date.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623278-1DAAE4A200000578-853_154x115.jpg" height="115" width="154" alt="Kaley" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Partner look: Kaley Cuoco and husband Ryan Sweeting are still in the honeymoon phase as they dress alike for a lunch date
            </strong>
            Together 11 months
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623331/Hilaria-Baldwin-pontificates-soapbox-Kim-Kardashians-wedding.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623331-1DAAF74E00000578-253_154x115.jpg" height="115" width="154" alt="Hilaria Baldwin" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            One small step for Hilaria Baldwin: Petite TV star stands on a soapbox in busy New York street, spilling latest gossip about  Kim Kardashian's wedding
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623287/It-dream-come-true-X-Factors-Simon-Cowell-teams-Australias-Animal-Logic-produced-The-LEGO-Movie-Happy-Feet.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623287-1DAB1CBA00000578-977_154x115.jpg" height="115" width="154" alt="Simon Cowell's Syco Entertainment announced a 'a long-term, multi-project partnership' with Australian animation and visual effects studio Animal Logic on Thursday" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'It is a dream come true': Simon Cowell teams up with Australian film company behind The LEGO Movie and Happy Feet
            </strong>
            Going into movies
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623317/Baby-number-two-Leelee-Sobieski-reveals-shes-pregnant-shows-large-bump-Dior-event.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623317-1DABFF0100000578-880_154x115.jpg" height="115" width="154" alt="Leelee" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Baby number two! Leelee Sobieski reveals she's pregnant again by showing off large bump at Dior event
            </strong>
            Child star of Eyes Wide Shut and Deep Impact
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622698/Tamara-Ecclestone-stands-red-carpet-thigh-skimming-zebra-print-dress-arrives-Gabrielles-Gala.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622698-1DAA8DFF00000578-412_154x115.jpg" height="115" width="154" alt="TAMARA ECCLESTONE" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            TAT's real love: Tamara Ecclestone shows off inked ode to husband Jay Rutland on her nape... while flashing her pins in thigh-skimming zebra-print dress
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622813/Hugh-Jackman-wears-band-aid-nose-spot-cancer-removed-year-trains-new-role-Peter-Pan.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622813-1DAA9DB500000578-503_154x115.jpg" height="115" width="154" alt="He's no Peter Pan! Hugh Jackman wears band-aid on his nose in the same spot he had cancer removed as he does boxing training for new film role" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            He's no Peter Pan! Hugh Jackman wears band-aid on his nose in the same spot he had cancer removed as he does boxing training for new film role
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/news/article-2622254/Katie-Price-brands-Jane-Pountney-homewrecker-husband-Derrick-plays-affair.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622254-1DA58DD700000578-101_154x115.jpg" height="115" width="154" alt="JANE MARIE POUNTNEY STORY- PICTURED BIRCH GROVE HOUSE WEST CHILTINGTON, WEST SUSSEX - KATIE PRICE ARRIVES AT THE HOUSE\\n\\n !!!!! PICTURE TAKEN ON PRIVATE ROAD !!!!!" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'It was more like a drunken kiss', says husband of Katie Price's best friend who model branded 'a wh*re homewrecker for 'affair' with her husband
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622744/Lindsay-Lohan-air-kisses-way-red-carpet-garish-plunging-peacock-frock-London-fundraiser.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622744-1DA69E0300000578-653_154x115.jpg" height="115" width="154" alt="Cringe! Lindsay Lohan air-kisses her way down the red carpet in garish plunging peacock frock at London fundraiser" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Cringe! Lindsay Lohan air-kisses her way down the red carpet in garish plunging peacock frock at London fundraiser
            </strong>
            You can take the girl out of Hollywood...
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623118/From-Pucci-Gucci-Rita-Ora-proves-wont-let-Gabrielles-Gala-switching-golden-gown-leather-outfit.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA9AB9600000578-330_154x115.jpg" height="115" width="154" alt="Rita Ora" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            From Pucci to Gucci: Rita Ora proves she won't let anyone down at Gabrielle's Gala switching from golden gown to leather outfit
            </strong>
            Showed some cleavage
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623196/The-Dream-claims-pregnant-ex-lover-Lydia-Nam-falsely-accused-assault-strangulation-avoid-deportation-US.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623196-1DAAA17100000578-719_154x115.jpg" height="115" width="154" alt="Dispute: Music producer The-Dream claims that assault allegations by his former partner Lydia Nam 'are lies to avoid being deported from the US'" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            The-Dream claims pregnant ex-lover Lydia Nam 'falsely accused him of assault and strangulation to avoid deportation from US'
            </strong>
            She's Canadian
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622594/Back-set-Jennifer-Lawrence-resumes-filming-Hunger-Games.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622594-1DA9B58D00000578-275_154x115.jpg" height="115" width="154" alt="HUNGER GAMES" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Katniss is back: Jennifer Lawrence resumes filming on her Hunger Games: Mockingjay movies as set moves from Atlanta to Paris
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2623329/An-close-personal-glimpse-inside-Met-Ball-secret-CAMERA-designer-Cynthia-Rowley-hid-purse.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623329-1DAD507200000578-189_154x115.jpg" height="115" width="154" alt="ROWLEY_PUFF.jpg" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            An up close and personal glimpse inside the Met Ball... from a secret CAMERA that designer Cynthia Rowley hid in her purse
            </strong>
            Clutch concealed GoPro
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623402/Hot-ticket-Dressed-low-key-chic-Lily-Collins-checks-screening-ex-Zac-Efron-new-comedy-movie-Neighbours.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623402-1DABF5FD00000578-276_154x115.jpg" height="115" width="154" alt="Lily Collins" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Hot ticket: Dressed in low-key chic Lily Collins checks out a screening of her ex Zac Efron in his new comedy movie Neighbours
            </strong>
            No ill-will between them
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623620/Boy-girl-Snooki-reveals-gender-second-baby-four-months.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623620-1DAD934D00000578-867_154x115.jpg" height="115" width="154" alt="Boy or girl? Snooki reveals gender of her second baby in touching video where she holds son Lorenzo" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Boy or girl? Snooki reveals gender of her second baby in touching video where she holds son Lorenzo
            </strong>
            She already has a son with Jionni LaValle
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622967/Racy-Rihanna-goes-demure-pink-dress-Dior-Cruise-Fashion-Show-Brooklyn.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622967-1DAAC32F00000578-408_154x115.jpg" height="115" width="154" alt="Good Girl Gone Stylish! Racy Rihanna goes demure in pink dress and silver jacket at the Dior Cruise Fashion Show in Brooklyn" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Good Girl Gone Stylish! Racy Rihanna goes demure in pink dress and silver jacket at the Dior Cruise Fashion Show in Brooklyn
            </strong>
            Pretty in pink
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622905/Coronation-Streets-Peter-Barlow-gets-fight-Steve-McDonald-turning-drunk-Tina-McIntyres-funeral.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622905-1DA878F500000578-670_154x115.jpg" height="115" width="154" alt="Coronation Street's Peter Barlow gets into a fight with Steve McDonald after turning up drunk to Tina McIntyre's funeral" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Coronation Street's Peter Barlow gets into a fight with Steve McDonald after turning up drunk to Tina McIntyre's funeral
            </strong>
            Funeral fracas
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623197/In-trouble-Justin-Bieber-gets-parking-ticket-outside-LA-theatre.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623197-1DAAB86F00000578-239_154x115.jpg" height="115" width="154" alt="Biebzatron" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            In trouble again: Justin Bieber gets a parking ticket outside LA theatre
            </strong>
            The 20-year-old Canadian singer was visiting Ivar Theatre
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2622954/SEBASTIAN-SHAKESPEARE-Pippa-Middletons-heel-hell-Ascot.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622954-1DA88B1100000578-107_154x115.jpg" height="115" width="154" alt="Pippa Middleton writes about her trip to Ascot races, pictured, in Vanity Fair's June edition" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            SEBASTIAN SHAKESPEARE: Pippa Middleton's heel hell at Ascot
            </strong>
            Advises wearing wedges in her latest writing attempt in Vanity Fair
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623243/Seth-Rogen-brightens-outfit-jolly-hat-enjoys-relaxing-stroll-wife-NYC.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623243-1DAA947100000578-925_154x115.jpg" height="115" width="154" alt="Seth Rogen and his wife Lauren Miller out walking their dog in New  York" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Cap that! Funnyman Seth Rogen brightens up outfit with a jolly colourful hat as he enjoys relaxing stroll with wife in NYC
            </strong>
            Time off the promo trail
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623097/Georgia-May-Jagger-opts-effortless-elegance-midnight-blue-thigh-split-pencil-dress-attends-charity-gala.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA9A06400000578-343_154x115.jpg" height="115" width="154" alt="Georgia May Jagger" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Georgia May Jagger opts for effortless elegance in a midnight blue thigh-split pencil dress as she attends charity gala
            </strong>
            Did her bit for cancer
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623058/Jada-Pinkett-Smith-arrives-LAX-leather-trousers-following-13-year-old-daughter-Willows-photo-scandal.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623058-1DAB46A300000578-506_154x115.jpg" height="115" width="154" alt="Jada Pinkett Smith arrives at LAX in leather trousers following 13-year-old daughter Willow's photo scandal" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Jada Pinkett-Smith insists there's 'nothing sexual' about picture of daughter Willow Smith, 13, lying in bed with Moises Arias, 20... as Jaden shows solidarity
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623134/One-Direction-swamped-fans-break-world-tour-visit-Christ-Redeemer-Statue-Brazil.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAA199E00000578-300_154x115.jpg" height="115" width="154" alt="One Direction swamped by fans as they take a break from world tour to visit Christ the Redeemer Statue in Brazil" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            The main attraction! One Direction swamped by fans as they take a break from world tour to visit Christ the Redeemer Statue in Brazil
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623286/Elviss-granddaughter-Riley-Keough-lends-arm-injured-boyfriend-walks-crutch.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623286-1DAB03D400000578-871_154x115.jpg" height="115" width="154" alt="Riley Keough who affectionately lent her injured boyfriend Ben Smith-Peterson her shoulder as the pair caught a cab in New York" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Love Me Tender: Elvis's granddaughter Riley Keough lends an arm to her injured boyfriend as he walks on crutch
            </strong>
            Lean On Me...&nbsp;
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622656/Spoiler-alert-24-things-learned-season-nine-premiere-24-Jim-Shelley.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622656-1DA4F76D00000578-645_154x115.jpg" height="115" width="154" alt="Jack Bauer (played by Kiefer Sutherland) is never more than seven minutes away from pointing a gun at someone in 24" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            SPOILER ALERT: 24 things we learned from the season nine premiere of 24, by Jim Shelley
            </strong>
            Jack is back... and this time, he's in London
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623123/Zac-Efron-joins-Jimmy-Fallon-The-Tonight-Show-hilarious-drag-skit.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623123-1DACC9DB00000578-305_154x115.jpg" height="115" width="154" alt="ZAC EFRON" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            He kept his trousers on this time! Zac Efron joins Jimmy Fallon on The Tonight Show after hilarious drag skit
            </strong>
            Wore a suit to discuss new movie Neighbours
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623408/Pharrell-Williams-reveals-hung-Michael-Jackson-twice-bizarre-phone-call-singer-turned-music.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623408-1DABF22E00000578-586_154x115.jpg" height="115" width="154" alt="King of popcorn! Pharrell Williams reveals he hung up on Michael Jackson twice during bizarre phone call with the singer after he turned down his music" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'King of popcorn!' Pharrell Williams reveals he hung up on Michael Jackson twice during bizarre phone call with the singer after he turned down his music
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622873/Kylie-Minogue-age-defying-returns-stage-racy-PVC-look.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622873-1DA9DC9F00000578-890_154x115.jpg" height="115" width="154" alt="Keeping it raunchy! Age defying Kylie Minogue makes debut on The Voice Italy in skin tight PVC skirt and bondage style top" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Keeping it raunchy! Age defying Kylie Minogue makes debut on The Voice Italy in skin tight PVC skirt and bondage style top
            </strong>
            Sexy as ever
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623200/Game-Of-Thrones-director-Alex-Graves-midst-sticky-divorce-wife-Sarah.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623200-1DAA5FF700000578-12_154x115.jpg" height="115" width="154" alt="'She refuses to let him see the kids...unless he gives her more money': Controversial Game Of Thrones director Alex Graves in the midst of sticky divorce from wife Sarah" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'She refuses to let him see the kids...unless he gives her more money': Controversial Game Of Thrones director Alex Graves in midst of sticky divorce from wife Sarah
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623068/Lily-Allen-shimmers-sparkly-star-embellished-dress-heads-night.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623068-1DA97FF600000578-985_154x115.jpg" height="115" width="154" alt="Shimmering: Lily Allen didn't disappoint on her first night out back in London since wowing on the red carpet at the Met Gala on Monday night as she dazzled in a glamorous sparkly dress for the evening" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Sheezus is a star! Lily Allen dazzles in sparkly embellished dress as she heads out for the night
            </strong>
            She's certainly returned to her party animal ways
          </span>
        </a>
      </li>
      <li>
        <a href="/news/article-2622491/Meet-seven-women-Bravos-Ladies-London-drinking-cat-fighting-royal-dropping-labor-scenes-coming-TV.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622491-1DAB161C00000578-574_154x115.jpg" height="115" width="154" alt="Ladies" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Royal name dropping, polo watching and lots of champagne: Meet the seven women from 'Ladies of London' set to take over television this summer
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/news/article-2622987/She-took-control-ended-pain-Julia-Roberts-harsh-bizarre-eulogy-estranged-sister-killed-herself.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622987-1DAB4E9100000578-892_154x115.jpg" height="115" width="154" alt="julia" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'She took control and ended her pain': Julia Roberts' 'harsh and 'bizarre' eulogy for estranged sister who killed herself
            </strong>
            Spoke unexepectedly&nbsp;
          </span>
        </a>
      </li>
      <li>
        <a href="/news/article-2622710/Dapper-Harry-arrives-Dorchester-minus-tie-girlfriend-celebrates-10th-anniversary-AIDS-charity-set-memory-mother-Princess-Diana.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/linkListItem-0-1DA73AB400000578-879_154x115.jpg" height="115" width="154" alt="Joss Stone, who recently visited some of the charity's projects in Africa and will entertain fellow guests. Other star turns include magician Troy and singer Beverley Knight" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Dapper Harry arrives at the Dorchester minus a tie (and a girlfriend) as he celebrates 10th anniversary of his AIDS charity with friend, singer Joss Stone
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622889/Alex-Reid-spends-quality-time-daughter-Dolly-offers-support-ex-Katie-Price.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622889-1DA841D200000578-435_154x115.jpg" height="115" width="154" alt="Daddy's girl: Alex Reid spends time with daughter Dolly" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'The best things in life are free': Alex Reid spends quality time with his daughter Dolly... as he offers support to ex Katie Price
            </strong>
            Suddenly the family man
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2623256/David-Beckham-Prince-George-luxury-brands-helping-hand-Britishness-cited-reason-buy-global-shoppers.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAAA25800000578-123_154x115.jpg" height="115" width="154" alt="british" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            David Beckham and Prince George give our luxury brands a helping hand: 'Britishness' cited as a reason to buy by global shoppers
            </strong>
            Big with Chinese market
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623210/Back-block-Maria-Shriver-spends-quality-family-time-youngest-son-Christopher-Schwarzenegger.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623210-1DAAD67700000578-246_154x115.jpg" height="115" width="154" alt="Shriver" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Back on the block: Maria Shriver spends some quality family time with her youngest son Christopher Schwarzenegger
            </strong>
            Out in Los Angeles
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623129/Leona-Lewis-works-black-cape-bold-structured-shoulders-Be-Beautiful-Be-Yourself-Gala.html" class="bottom">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623129-1DA9F57900000578-663_154x115.jpg" height="115" width="154" alt="Leona Lewis went for a twist on a classic look with pointed power shoulders as she attended the Be Beautiful Be Yourself Gala." />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            She's got the power! Leona Lewis works black cape with bold pointed shoulders at Be Beautiful Be Yourself Gala
            </strong>
            Opted for all-black
          </span>
        </a>
      </li>
    </ul>
    
  </div>

  </div>
  <script type="text/javascript">
    DM.has('p-604', 'comScore', {
      mo_mod_id: '1000113',
      mo_mod_pos: 'p-604'
    });
  </script>

  </div>
  </div>
    <div class="gamma">
        <div class="item video_carousel_module_wrapper">
    <div class="home  video_carousel_container cleared" id="p-607"
       data-track-module="sm-726^video_carousel_module"
       data-track-selector=".videoLink"
       data-track-type="cl">
      <div class="video_carousel_title bdrcc">
        <div class="wocc carousel-title">VIDEO</div>
        <img src="http://i.dailymail.co.uk/i/furniture/standard_modules/video/icon_filmstrip.png" />
        <div class="channel-title">WATCH: TODAY'S TOP VIDEOS</div>
        <div class="rotator-title">
          <ul class="rotator-pages">
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="1"><span class="usability">1</span></a>
            </li>
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="2"><span class="usability">2</span></a>
            </li>
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="3"><span class="usability">3</span></a>
            </li>
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="4"><span class="usability">4</span></a>
            </li>
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="5"><span class="usability">5</span></a>
            </li>
          </ul>
        </div>
      </div>

      <div class="video-carousel-body">
        <div class="link-wox linkro-ccox left">
          <a class="js-move-prev" href="#">
            <div class="left_scroll"><span></span></div>
          </a>
          <div class="blank-div"></div>
        </div>
        <div class="rotator link-wocc linkro-womlcc">
          <ul class="js-itemList rotator-panels">
            <li class="item">
              <a class="videoLink" href="/video/news/video-1093958/Girl-clobbers-rival-head-SHOVEL.html"
                data-videoid="3543571385001"
                data-channel="news"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093958&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA4E8EE00000578-634_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>78995</p></div>
                <div class="video-item-title bdrcc">Girl clobbers her rival in the head with SHOVEL after cat fight escalates</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/news/video-1093978/Kieran-Hayler-leaves-Jane-Poutneys-house-Katie-meeting.html"
                data-videoid="3544089391001"
                data-channel="news"
                data-source="Splash"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093978&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA5E97200000578-977_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>41727</p></div>
                <div class="video-item-title bdrcc">Kieran Hayler leaves Jane Poutney's house after meeting with wife Katie Price</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/news/video-1094067/Video-claims-UFO-attacking-Taliban-base.html"
                data-videoid="3546130209001"
                data-channel="news"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094067&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DAA250D00000578-708_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>62741</p></div>
                <div class="video-item-title bdrcc">Video claims to show footage filmed by US armed forces of a UFO 'attacking a Taliban base'</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/news/video-1094054/GRAPHIC-Body-cam-captures-harrowing-domestic-abuse-attack.html"
                data-videoid="3546024451001"
                data-channel="news"
                data-source="Met Police"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094054&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA9C39100000578-360_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>84962</p></div>
                <div class="video-item-title bdrcc">New Metropolitan Police body cameras capture harrowing domestic abuse attack</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/news/video-1093386/Terrifying-moment-man-knocked-dragged-GHOST.html"
                data-videoid="3532836293001"
                data-channel="news"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093386&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/03/video-undefined-1D8A3AA600000578-59_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>60512</p></div>
                <div class="video-item-title bdrcc">Did you see that?! Terrifying moment man is knocked down and dragged by a GHOST</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/news/video-1093924/Man-grabs-stripper-home-private-performance.html"
                data-videoid="3543616291001"
                data-channel="news"
                data-source="Other"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093924&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA51E2700000578-288_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>39168</p></div>
                <div class="video-item-title bdrcc">Shocking footage of man who waited for stripper outside club and snatches her to take home...</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/sciencetech/video-1093939/Ralphee-wobbly-Kitten-inseparable-Max-dog.html"
                data-videoid="3543351818001"
                data-channel="sciencetech"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093939&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA4348A00000578-511_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>84289</p></div>
                <div class="video-item-title bdrcc">Ralphee the kitten and Max the cattle dog are an odd couple who seem besotted with each...</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1093968/Kerry-Katona-shows-baby-number-traumatic-birth.html"
                data-videoid="3543795860001"
                data-channel="tvshowbiz"
                data-source="ITV"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093968&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA5557000000578-43_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>29327</p></div>
                <div class="video-item-title bdrcc">Kerry Katona shows off baby number five after traumatic birth and she says she may not be...</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/news/video-1084844/Horror-moment-Andrew-Young-floored-single-fatal-punch.html"
                data-videoid="3254160254001"
                data-channel="news"
                data-source="BNPS"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1084844&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/02/25/video-undefined-1BD0F25400000578-82_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>58640</p></div>
                <div class="video-item-title bdrcc">Horror moment Andrew Young is floored by single, fatal punch</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/news/video-1094057/Body-cam-captures-suspects-surprisingly-honest-confesssion.html"
                data-videoid="3546054295001"
                data-channel="news"
                data-source="Police"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094057&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA9DB6F00000578-70_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>35968</p></div>
                <div class="video-item-title bdrcc">Police body cam captures burglary and stabbing suspect's surprisingly honest confession</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/news/video-1093764/Emilys-video-diary-footage-abortion-procedure.html"
                data-videoid="3541022910001"
                data-channel="news"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093764&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/06/video-undefined-1D9D6C3B00000578-500_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>180605</p></div>
                <div class="video-item-title bdrcc">Emily's emotional before video diary and footage of her abortion procedure</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1093961/Best-friend-Jane-Katies-marries-Kieran.html"
                data-videoid="3543616251001"
                data-channel="tvshowbiz"
                data-source="Splash"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093961&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA5141A00000578-379_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>100496</p></div>
                <div class="video-item-title bdrcc">Best friend Jane Pountney by Katie's side as she marries Kieran Hayler</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/femail/video-1094046/Based-true-story-Heaven-Is-For-Real-trailer.html"
                data-videoid="3545978612001"
                data-channel="femail"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094046&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA9827700000578-963_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>165628</p></div>
                <div class="video-item-title bdrcc">America gripped by story of little boy who says he went to Heaven then came back</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1094006/Jordanian-TV-guests-destroy-7-stars-news-studio-live-show.html"
                data-videoid="3545886210001"
                data-channel="tvshowbiz"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094006&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA9704C00000578-324_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>26494</p></div>
                <div class="video-item-title bdrcc">Jordanian TV guests destroy the 7 stars news studio during live show</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/news/video-1093627/Boob-grabbing-Clippers-fan-new-Katherine-Webb.html"
                data-videoid="3538655378001"
                data-channel="news"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093627&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/05/video-undefined-1D97409F00000578-272_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>43236</p></div>
                <div class="video-item-title bdrcc">Boob-grabbing Clippers fan Rebecca Grant is the new Katherine Webb</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/news/video-1093949/Children-thrown-fourth-floor-window-cuts-escape-route.html"
                data-videoid="3543415365001"
                data-channel="news"
                data-source="Other"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093949&amp;colour=home&amp;item-type=sm&amp;item-id=726 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA47AE900000578-172_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>52803</p></div>
                <div class="video-item-title bdrcc">Shocking moment woman throws her children thrown from fourth floor window as fire cut off...</div>
              </a>
            </li>
          </ul>
        </div>
        <div class="link-wox linkro-ccox right">
          <a class="js-move-next" href="#">
            <div class="right_scroll"><span></span></div>
          </a>
          <div class="blank-div"></div>
        </div>
      </div>
  </div>
  <script type="text/javascript">
  DM.has("p-607", 'videoChannelCarouselModule',
         {"player" : "1989148206001",
          "playerKey" : "AQ~~,AAAAAFSL1bg~,CmS1EFtcMWELN_eSE9A7gpcGWF5XAVmI",
          "nonEmbeddablePlayerIdent" : "2572801325001",
          "nonEmbeddablePlayerKey" : "AQ~~,AAAAAFSL1bg~,CmS1EFtcMWF3nDd2YNUcSIWL0H_o4As-",
          "trackingType" : "carousel_triple",
          "channelShortName" : "home",
          "overlayType" : "carousel",
          "pageCount" : "5",
          "pageSize" : 3,
          "onPos": 0,
          "updateStyleOnHover": true,
          "videoPlayerConfigMap": {'3543571385001' : 'false','3544089391001' : 'false','3546130209001' : 'false','3546024451001' : 'false','3532836293001' : 'false','3543616291001' : 'false','3543351818001' : 'false','3543795860001' : 'false','3254160254001' : 'false','3546054295001' : 'false','3541022910001' : 'false','3543616251001' : 'false','3545978612001' : 'false','3545886210001' : 'false','3538655378001' : 'false','3543415365001' : 'false'},
          "rsi" : typeof(adverts) != 'undefined' && typeof (adverts.getRsiValues) != 'undefined' ? adverts.getRsiValues() : null
  });
  </script>


  </div>

        <div class="home item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

  </div>
    <div class="cleared">
        <div class="alpha">
     <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline51}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623122/B-reem-TV-bosses-dont-think-Chip-shop-owners-facing-legal-action-Towie-production-firm-naming-restaurant-The-Only-Way-Fish.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623122-1DAA25DC00000578-80_636x382.jpg" height="382" width="636" alt="The Only Way is Fish" />
        </a>
      <div >
       <p>
         
         Francesca Clark was stunned when she received a letter from Lime Pictures ordering her to change the name of her Essex chip shop within 14 days. The chip shop owner said she had deliberately created a restaurant with a 'cheesy, blingy and glitzy' decor and used a logo similar to the one used for Towie, but was told by the TV production company that the shop's name had copyrighted 'The Only Way is'.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623122/B-reem-TV-bosses-dont-think-Chip-shop-owners-facing-legal-action-Towie-production-firm-naming-restaurant-The-Only-Way-Fish.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623122">         184</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEPNqK| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623122-1DAA25DC00000578-80_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline52}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623401/Jenny-Willott-I-hate-PMQs-total-passion.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623401-02BC1F650000044D-465_154x115.jpg" height="84" width="112" alt="Lib Dem minister Jenny Willott" />
      </a>
      <p>
        
        The Business Minister, who attends Cabinet on women's issues. also lifted the lid on the 'massive rows' she has had with senior Lib Dems about the failure elect more female MPs.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623401/Jenny-Willott-I-hate-PMQs-total-passion.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623401">          82</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFLj3m| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623401-02BC1F650000044D-376_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline53}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2622603/Michelle-Knight-reveals-Ariel-Castro-hit-jaw-barbell.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622603-1DA6592900000578-66_112x84.jpg" height="84" width="112" alt="Michelle" />
      </a>
      <p>
        
        The horrifying details emerged in Michelle Knight's book Finding Me which was published on May 6.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2622603/Michelle-Knight-reveals-Ariel-Castro-hit-jaw-barbell.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622603">         307</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2622603/Michelle-Knight-reveals-Ariel-Castro-hit-jaw-barbell.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1inbhEP| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622603-1DA608BD00000578-875_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline54}}</a>
    </h2>
    <div class="articletext">
      <a href="/money/cars/article-2623451/Councils-dealing-deluge-pothole-compensation-claims.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DACDDA200000578-692_154x115.jpg" height="84" width="112" alt="Pothole plague: This new sign, designed by the campaign website, aims to warn motorists of potentially dangerous pothole-plagued roads" />
      </a>
      <p>
        
        Thousands of drivers up and down the country are demanding compensation for car axle, wheel and suspension faults caused by pothole-plagued stretches of roads.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="ThisIsMoney">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/money/cars/article-2623451/Councils-dealing-deluge-pothole-compensation-claims.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623451">          16</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuMAvQ| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DACDDA200000578-742_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline55}}</a>
    </h2>
    <div class="articletext">
      <a href="/femail/article-2623434/British-parents-eight-years-worth-sleepless-Nights-Time-Their-Child-Turns-30.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623434-1DAD171200000578-510_156x119.jpg" height="84" width="112" alt="sleepless" />
      </a>
      <p>
        
        While you might think the disturbed nights ease off as the infant grows up, research shows most lose sleep more when their child is an adult.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="Femail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/femail/article-2623434/British-parents-eight-years-worth-sleepless-Nights-Time-Their-Child-Turns-30.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623434">           4</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFRZ1o| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623434-1DAD171200000578-543_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline56}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623194/Married-gay-couples-official-coats-arms-College-Arms-pass-colleges-strict-seal-approval-first.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623194-00E8C9D100000190-452_154x115.jpg" height="84" width="112" alt="Sir Elton John, who is believed to be marrying his civil partner David Furnish in private this month, currently holds an 'escutcheon', or shield, featuring a keyboard, records and a satyr playing pan pipes" />
      </a>
      <p>
        
        For centuries, married couples have been designing shared escutcheons that combine their family histories in one heraldic symbol. But the strict rules of the ancient body meant civil partners could not qualify.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623194/Married-gay-couples-official-coats-arms-College-Arms-pass-colleges-strict-seal-approval-first.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623194">          13</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru6pmY| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623194-1DAB3BAF00000578-918_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline57}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623445/Aisle-voting-Asda-mums-reveal-shopping-list-election-demands-including-energy-bills-childcare-end-political-jargon.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623445-1DAB913000000578-64_154x115.jpg" height="84" width="112" alt="Two thirds of mums said they wanted action on energy bills, a key promise made by Labour's Ed Miliband&amp;nbsp;" />
      </a>
      <p>
        
        Just one in 10 mums think politicians have their best interests at heart, according to the Asda Mumdex survey. Three-quarters think policies are too male-centric.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623445/Aisle-voting-Asda-mums-reveal-shopping-list-election-demands-including-energy-bills-childcare-end-political-jargon.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623445">           7</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuKHit| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623445-1DAB913000000578-181_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline58}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623162/Megamouth-shark-cut-open-crowd-1500-onlookers.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623162-1DAD791B00000578-673_636x382.jpg" height="382" width="636" alt="shark" />
        </a>
      <div >
       <p>
         
         This rare sea creature (left) was hauled up from more than 800m beneath a Japanese ocean - and was given a public autopsy (top right) at Shizuoka Marine Science Museum. Crowds gathered to see the beast - a whopping four metres long - and even came face to face with slices of its flesh which were paraded round the premises (bottom right).
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623162/Megamouth-shark-cut-open-crowd-1500-onlookers.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623162">          43</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623162/Megamouth-shark-cut-open-crowd-1500-onlookers.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mGaAu6| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623162-1DAD791B00000578-673_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline59}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623289/Disgraced-Crystal-Methodist-Paul-Flowers-allowed-live-RENT-FREE-church-owned-house-continues-paid-11-106-year.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622225-1DA28AEB00000578-743_154x115.jpg" height="84" width="112" alt="Former Co-operative Bank boss Paul Flowers today pleaded guilty at Leeds Magistrates' Court to drugs possession" />
      </a>
      <p>
        
        The cleric has been allowed to return to the £300,000 home in Bradford bestowed to him by Methodist church leaders while they carry out an independent investigation.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623289/Disgraced-Crystal-Methodist-Paul-Flowers-allowed-live-RENT-FREE-church-owned-house-continues-paid-11-106-year.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623289">           5</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623289/Disgraced-Crystal-Methodist-Paul-Flowers-allowed-live-RENT-FREE-church-owned-house-continues-paid-11-106-year.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFlfoO| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622225-1DA28AEB00000578-15_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline60}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623378/Original-pencil-drawings-genius-Mulberry-harbours-vital-D-Day-landings-auction.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623378-1DAACFBB00000578-665_154x115.jpg" height="84" width="112" alt="The original plans for the Mulberry harbour invention that allowed the Allied invasion of France on D-Day are expected to fetch £60,000 at auction. They were designed by Welsh engineer Hugh Iorys Hughes" />
      </a>
      <p>
        
        The secret wartime plans are being offered by an anonymous American collector and are expected to raise between £40,000 and £60,000.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623378/Original-pencil-drawings-genius-Mulberry-harbours-vital-D-Day-landings-auction.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623378">           5</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ruy3QE| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623378-1DAACFBB00000578-889_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline61}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623339/I-criminal-records-check-host-foreign-student-HE-turned-sex-offender-Fury-father-Czech-exchange-let-paedophile-home.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623339-1DAB678400000578-172_154x115.jpg" height="84" width="112" alt="Jailed: Paedophile language student Zdenek Junek did not have his record checked - but his hosts did" />
      </a>
      <p>
        
        Wayne Beavill, 44, and his wife Sharon, 43, were horrified when police visited their home in Brighton, West Sussex, after they took in student Zdenek Junek (pictured).
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623339/I-criminal-records-check-host-foreign-student-HE-turned-sex-offender-Fury-father-Czech-exchange-let-paedophile-home.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623339">          17</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFtxxb| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623339-1DAB9D2D00000578-899_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline62}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623237/My-Big-Fat-Gypsy-Wedding-star-escapes-punishment-driving-without-insurance-getting-wife-check-documents-barely-read.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623237-1DAA449E00000578-291_154x115.jpg" height="84" width="112" alt="William Henry Welch, 53, escaped punishment for driving without licence because his wife incorrectly told him he would be covered if he borrowed a friend's car" />
      </a>
      <p>
        
        William Henry Welch, 53, avoided six penalty points on his driving licence because his wife incorrectly told him he would be covered if he borrowed a friend's car.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623237/My-Big-Fat-Gypsy-Wedding-star-escapes-punishment-driving-without-insurance-getting-wife-check-documents-barely-read.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623237">          81</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mF7Mxw| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623237-1DAA449E00000578-350_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline63}}</a>
    </h2>
    <div class="articletext">
      <a href="/money/mortgageshome/article-2623351/Labour-want-ban-letting-agents-fees-stand-tenants.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-0671EFA400000514-965_154x115.jpg" height="84" width="112" alt="Rental fightback: Labour leader Ed Miliband wants to overhaul rules to help tenants" />
      </a>
      <p>
        
        Ed Miliband, Labour leader, says he is ‘determined to stand up for generation rent’ and deliver an ‘immediate financial benefit’ to tenants.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="ThisIsMoney">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/money/mortgageshome/article-2623351/Labour-want-ban-letting-agents-fees-stand-tenants.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623351">         114</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFyIx0| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-0671EFA400000514-61_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline64}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623041/Spring-postponed-Gale-force-winds-50mph-batter-Britain-two-days-heavy-rain-set-sweep-west.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623041-004B470900000258-162_154x115.jpg" height="84" width="112" alt="Gusts of up to 50mph are expected to hit the south coast today, tomorrow and into the weekend" />
      </a>
      <p>
        
        Forecasters are predicting around 10mm of rain could fall in an hour in parts of the south and west today and tomorrow, with gusts reaching up to 50mph
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623041/Spring-postponed-Gale-force-winds-50mph-batter-Britain-two-days-heavy-rain-set-sweep-west.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623041">         163</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtlYew| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623041-004B470900000258-620_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline65}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623217/The-tale-two-disasters-Eerie-photos-left-Japanese-city-abandoned-tsunami-Fukushima-nuclear-disaster.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623217-1DA8D55F00000578-397_636x382.jpg" height="382" width="636" alt="Empty platforms: The images, including those of the empty station,  were caught on a drone which hovered over the abandoned community" />
        </a>
      <div >
       <p>
         
         More than 15,000 residents living in 6,000 houses were forced to evacuate the city of Tomioka in March 2011 because of safety fears concerning dangerous radiation levels. It was a city known for its beautiful beaches in the summer and boasted one of the longest cherry blossom tree tunnels in Japan. But after a devastating tsunami and the Fukushima nuclear disaster both struck in the space of 12 months, it was turned into a ghost city. A fishing vessel that was washed ashore has been left on the side of a road for three years (top left) and the city's train station has been covered by overgrown grass (bottom left).
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623217/The-tale-two-disasters-Eerie-photos-left-Japanese-city-abandoned-tsunami-Fukushima-nuclear-disaster.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623217">          86</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623217/The-tale-two-disasters-Eerie-photos-left-Japanese-city-abandoned-tsunami-Fukushima-nuclear-disaster.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://www.dailymail.co.uk/news/article-2623217/The-tale-two-disasters-Eerie-photos-left-Japanese-city-abandoned-tsunami-Fukushima-nuclear-disaster.html| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623217-1DAB378A00000578-161_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline66}}</a>
    </h2>
    <div class="articletext">
      <a href="/travel/article-2623220/Inside-Conrad-Maldvies-Hotels-worlds-glass-underwater-restaurant-five-metres-BELOW-Indian-Ocean.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623220-1DA9F40B00000578-658_154x115.jpg" height="84" width="112" alt="Panoramic views: The Ithaa restaurant ceiling has been built in giant glass arches, meaning guests can enjoy dinner surrounded by sharks and other sealife" />
      </a>
      <p>
        
        Boasting unrivalled views, the five-star eatery at the Conrad Maldives Hotel was built so that guests can enjoy the beauty of the ocean without getting their feet wet.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="travelmail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/travel/article-2623220/Inside-Conrad-Maldvies-Hotels-worlds-glass-underwater-restaurant-five-metres-BELOW-Indian-Ocean.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623220">         107</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/travel/article-2623220/Inside-Conrad-Maldvies-Hotels-worlds-glass-underwater-restaurant-five-metres-BELOW-Indian-Ocean.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mF54ba| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623220-1DAAD76A00000578-359_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline67}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623494/Former-headteacher-year-faces-classroom-ban-tens-thousands-pounds-false-expenses-claims-including-7-000-lavish-birthday-party.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DABC76700000578-412_154x115.jpg" height="84" width="112" alt="Jo Shuter and Quintin Kynaston school in St John's Wood, London" />
      </a>
      <p>
        
        Jo Shuter (left) has admitted unprofessional conduct after a string of false expenses claims while she was in charge of a north London school (right).
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623494/Former-headteacher-year-faces-classroom-ban-tens-thousands-pounds-false-expenses-claims-including-7-000-lavish-birthday-party.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623494">           0</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mG3QMN| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DABC76700000578-27_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline68}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623304/How-poachers-use-INSTAGRAM-prey-Geo-tagged-photos-help-hunters-track-injure-kill-tigers-elephants-rhinos.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623304-1DAB002D00000578-287_154x115.jpg" height="84" width="112" alt="This photo posted on Twitter this week by Eleni de Wet in South Africa reveals just how much of a concern geo-tagged tourist photos have become in the battle against poachers" />
      </a>
      <p>
        
        A photo tweeted by Eleni de Wet in South Africa this week reveals how tourists are unwittingly sending the physical coordinates of safari animals to poachers.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623304/How-poachers-use-INSTAGRAM-prey-Geo-tagged-photos-help-hunters-track-injure-kill-tigers-elephants-rhinos.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623304">           5</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFC4jG| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623304-1DAB002D00000578-619_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline69}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623430/Taking-selfies-just-got-sharper-Super-sensor-adds-digital-camera-style-optical-zoom-gadgets.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623430-1DABB75D00000578-550_154x115.jpg" height="84" width="112" alt="Engineers from Israel designed the dual-lens system to make it small enough to fit in a smartphone. The technology is capable of achieving an optical zoom five times greater than 3x digital zoom and is also used to create depth of field effects that can be altered after the shot has been taken" />
      </a>
      <p>
        
        The Israeli system achieves an optical zoom five times greater than 3x digital zoom and is also used to create depth of field effects that can be edited.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623430/Taking-selfies-just-got-sharper-Super-sensor-adds-digital-camera-style-optical-zoom-gadgets.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623430">           4</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mGcMlf| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623430-1DAD252500000578-333_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline70}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623542/Could-drones-save-nuclear-waste-Unmanned-aircraft-fly-toxic-materials-safe-locations.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623542-1DAD3A1600000578-778_154x115.jpg" height="84" width="112" alt="A team of engineers led by Dr Mirko Kovac at the Aerial Robotics Laboratory at Imperial College London have revealed their flying robots that can transport nuclear waste to safe locations by spraying it with foam and sticking to it" />
      </a>
      <p>
        
        A team of engineers have created what they call 'flying 3D printing robots'. The project is led by Dr Mirko Kovac at Imperial College London.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623542/Could-drones-save-nuclear-waste-Unmanned-aircraft-fly-toxic-materials-safe-locations.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623542">           4</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/sciencetech/article-2623542/Could-drones-save-nuclear-waste-Unmanned-aircraft-fly-toxic-materials-safe-locations.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mGc9bs| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623542-1DAD3A1600000578-255_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline71}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623131/Primary-school-Europe-introduce-desks-allowing-children-stand-working.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623131-1DA9D08500000578-683_154x115.jpg" height="84" width="112" alt="Pilot: Aleefa, ten, is one of the pupils at Grove House Primary School in Bradford using a standing desk" />
      </a>
      <p>
        
        Nine and ten-year-old pupils at Grove House Primary School in Bradford, West Yorkshire, are taking part in the pilot run by local medical researchers.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623131/Primary-school-Europe-introduce-desks-allowing-children-stand-working.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623131">          56</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623131/Primary-school-Europe-introduce-desks-allowing-children-stand-working.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEZl5d| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623131-1DAA885400000578-348_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline72}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623249/The-suns-power-glory-Nasa-captures-best-images-powerful-solar-X-flare.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623249-1DAA60C300000578-862_154x115.jpg" height="84" width="112" alt="Nasa has released imagery and data from a huge solar flare on 29 March 2014 that was observed by its fleet of spacecraft. This image from the Iris spacecraft shows material some 650 miles above the sun's surface. The vertical line in the middle shows the slit for the spectrograph, which can separate light into its wavelengths" />
      </a>
      <p>
        
        Five Nasa observatories have taken unprecedented images of a solar flare. It was only be chance that they all saw the huge event at the same time.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623249/The-suns-power-glory-Nasa-captures-best-images-powerful-solar-X-flare.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623249">          24</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/sciencetech/article-2623249/The-suns-power-glory-Nasa-captures-best-images-powerful-solar-X-flare.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFh7oQ| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623249-1DAB1D5500000578-434_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline73}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623262/Nasa-creates-STARDUST-Earth-Cosmic-machine-helps-scientists-understand-material-makes-galaxies.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623262-1DAA9A3E00000578-323_154x115.jpg" height="84" width="112" alt="A close up iimage interstellar dust created by the Cosmic machine. This grain is approximately 1.5 micrometers in diameter. For comparison, a bacteria cell is around 5 micrometers" />
      </a>
      <p>
        
        The Cosmic simulator in California was able to create particles of interstellar dust at 1.5 micrometres, or about a tenth of the width of a human hair.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623262/Nasa-creates-STARDUST-Earth-Cosmic-machine-helps-scientists-understand-material-makes-galaxies.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623262">           5</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Rued83| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623262-1DAB077400000578-813_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline74}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623509/State-art-RV-boasts-eight-flat-screen-TVs-sky-lounge-rooftop-tanning-beds-fireplaces-eye-watering-starting-price-1million-pay-gas-parking-spot.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623509-1DAD84D700000578-744_636x382.jpg" height="382" width="636" alt="RV" />
        </a>
      <div >
       <p>
         
         A range of luxury RVs have hit the market with an eye-watering starting price tag of $1,374,451 but they are a whole different breed to the campers snow-haired retirees favored in the 1970s. Rather than just a place to sleep while on the road, these mobile mansions have more amenities than your average Hamptons summer rental, decked out with upright pianos, treadmills, tanning beds, recording studios for musician types, and fireplaces.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623509/State-art-RV-boasts-eight-flat-screen-TVs-sky-lounge-rooftop-tanning-beds-fireplaces-eye-watering-starting-price-1million-pay-gas-parking-spot.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623509">          26</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623509/State-art-RV-boasts-eight-flat-screen-TVs-sky-lounge-rooftop-tanning-beds-fireplaces-eye-watering-starting-price-1million-pay-gas-parking-spot.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Rv6l6j| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623509-1DAD6A5200000578-350_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline75}}</a>
    </h2>
    <div class="articletext">
      <a href="/femail/article-2623344/Childbirth-lasts-hours-pain-relegation-lasts-summer-Two-thirds-football-fans-think-seeing-club-demoted-hurts-giving-birth.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623344-1DABAE7500000578-634_154x115.jpg" height="84" width="112" alt="relegation" />
      </a>
      <p>
        
        Even the less committed fans, who attended only one game per season, agreed that relegation was the male equivalent to childbirth.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="Femail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/femail/article-2623344/Childbirth-lasts-hours-pain-relegation-lasts-summer-Two-thirds-football-fans-think-seeing-club-demoted-hurts-giving-birth.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623344">          42</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuD9wa| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623344-1DABAE7500000578-811_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline76}}</a>
    </h2>
    <div class="articletext">
      <a href="/femail/article-2623283/Nine-10-women-never-wear-clothes-including-EIGHT-pairs-shoes-holiday-men-wear-90-theirs.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623283-1DAB3D2E00000578-906_154x115.jpg" height="84" width="112" alt="Couple trying to close full suitcase --- Image by © 237/Daly and Newton/Ocean/Corbis" />
      </a>
      <p>
        
        The majority of men on the other hand use at least 90% of what they’ve packed while away on holiday - and 53% of women's bags are overweight.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="Femail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/femail/article-2623283/Nine-10-women-never-wear-clothes-including-EIGHT-pairs-shoes-holiday-men-wear-90-theirs.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623283">          19</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFqHZ2| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623283-1DAB3D2E00000578-733_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline77}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623006/Elderly-head-one-Monacos-richest-families-fighting-life-hospital-mystery-mafia-style-shooting-Nice.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623006-1DA1A8B800000578-674_154x115.jpg" height="84" width="112" alt="Forensic experts investigate the car in which Helene Pastor was injured on Tuesday night" />
      </a>
      <p>
        
        The chauffeur-driven car of Helene Pastor, 77, was approached by a gunman who opened fire with a shotgun on Tuesday night, it is reported
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623006/Elderly-head-one-Monacos-richest-families-fighting-life-hospital-mystery-mafia-style-shooting-Nice.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623006">          19</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1iplXme| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623006-1DA1A8B800000578-604_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline78}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623092/Social-worker-assessed-Pistorius-hours-shot-Reeva-tells-trial-heartbroken.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623092-1DAA5DE000000578-352_154x115.jpg" height="84" width="112" alt="Pistorius preview" />
      </a>
      <p>
        
        Yvette van Schalkwyk said she felt compelled to give evidence after reading reports that Pistorius allegedly took acting lessons for his trial in Pretoria.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623092/Social-worker-assessed-Pistorius-hours-shot-Reeva-tells-trial-heartbroken.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623092">          65</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623092/Social-worker-assessed-Pistorius-hours-shot-Reeva-tells-trial-heartbroken.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru6syV| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623092-1DAB670F00000578-860_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline79}}</a>
    </h2>
    <div class="articletext">
        <a href="/femail/article-2623174/The-five-year-old-boy-banned-church-likes-wear-pretty-dresses.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623174-1DAA533A00000578-204_636x382.jpg" height="382" width="636" alt="Romeo Clarke" />
        </a>
      <div >
       <p>
         
         The playgroup says: 'Romeo will be welcome back when he wears clothes which match his gender.' His mother, Georgina Clarke, from Rugby, has lodged a complaint. The stay-at-home single mother says: 'Wearing the dress is his choice and if wearing it makes him happy, it's fine with me. He’s a normal boy who, because he has three big sisters, likes wearing dresses. What is wrong with that?'
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="Femail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/femail/article-2623174/The-five-year-old-boy-banned-church-likes-wear-pretty-dresses.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623174">         207</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/femail/article-2623174/The-five-year-old-boy-banned-church-likes-wear-pretty-dresses.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEXOw2| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623174-1DAADED200000578-842_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline80}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623582/Cigarette-filters-banned-experts-claim-butts-damaging-environment.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623582-1DAD6FD600000578-178_154x115.jpg" height="84" width="112" alt="Environmental experts claim cigarette butts, stock image pictured, contain the same toxins found in cigarettes and cigars, and can contaminate the environment and water sources. Researchers from San Diego are now calling for the cigarettes filters to be banned and propose tobacco companies put warnings on packets" />
      </a>
      <p>
        
        Experts claim cigarette butts contaminate the environment and water sources. Researchers from San Diego are calling for the filters to be banned.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623582/Cigarette-filters-banned-experts-claim-butts-damaging-environment.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623582">          27</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mGfVBA| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623582-1DAD6FD600000578-922_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline81}}</a>
    </h2>
    <div class="articletext">
      <a href="/health/article-2623271/Widow-sued-GP-1-25-million-misdiagnosed-husbands-deadly-cancer-PILES-wins-case-high-court.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/02/23/article-2566105-1BC2434300000578-15_154x115.jpg" height="84" width="112" alt="Mr Goodhead and his wife received the horrifying news that he was suffering from stage four cancer in June 2007" />
      </a>
      <p>
        
        Christopher Goodhead, who was described as 'fit and determined', died aged just 41 in January 2009 - four years after the examination by Dr Asim Islam.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/health/article-2623271/Widow-sued-GP-1-25-million-misdiagnosed-husbands-deadly-cancer-PILES-wins-case-high-court.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623271">           3</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFyaXQ| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/02/23/article-2566105-1BC460F600000578-822_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline82}}</a>
    </h2>
    <div class="articletext">
      <a href="/travel/article-2623266/Couple-forced-stay-cabin-48-hours-falling-ill-vomiting-bug-luxury-TUI-Island-Escape-cruise-awarded-1-300-payout.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623266-1DA466EE00000578-981_154x115.jpg" height="84" width="112" alt="'Locked on board': Shaun and Elizabeth Shields claim they were treated 'like dogs' on the Island Escape" />
      </a>
      <p>
        
        Shaun and Elizabeth Shields, of Braunstone, Leicester, said they were not allowed to leave their room as staff attempted to tackle an outbreak of norovirus on the ship, Island Escape.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="travelmail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/travel/article-2623266/Couple-forced-stay-cabin-48-hours-falling-ill-vomiting-bug-luxury-TUI-Island-Escape-cruise-awarded-1-300-payout.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623266">          96</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFgko6| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623266-1DA466EE00000578-310_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline83}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623209/Russia-plans-colonise-MOON-2030-according-leaked-government-document-says-robot-rovers-sent-2016.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623209-1AA752ED00000578-330_154x115.jpg" height="84" width="112" alt="Red dawn? Russian cosmonauts could be living on the Moon by 2030" />
      </a>
      <p>
        
        A draft government programme proposes a three-step plan to explore the Moon that would culminate in building a permanent Earth-monitoring observatory.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623209/Russia-plans-colonise-MOON-2030-according-leaked-government-document-says-robot-rovers-sent-2016.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623209">         113</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru31IC| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623209-1AA752ED00000578-649_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline84}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623124/Saudi-court-sentences-liberal-blogger-ten-years-jail-1-000-lashes-orders-pay-133-000-fine-insulting-Islam.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623124-1DAA25D000000578-614_154x115.jpg" height="84" width="112" alt="'Prisoner of conscience': Saudi blogger Raif Badawi" />
      </a>
      <p>
        
        Saudi Liberal Network founder Raif Badawi originally faced seven years jail, but was retried after an appeal court overturned that sentence. (Saudi King Abdullah is pictured)
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623124/Saudi-court-sentences-liberal-blogger-ten-years-jail-1-000-lashes-orders-pay-133-000-fine-insulting-Islam.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623124">         112</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEQqkj| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623124-1DAA25D000000578-182_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline85}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2622735/Abu-Hamza-claim-kept-Britain-safe-MI5-Scotland-Yard-takes-stand-New-York.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622735-1D1BCAB200000578-801_154x115.jpg" height="84" width="112" alt="Abu Hamza will argue that he attempted to keep London's streets safe by acting as an intermediary with British intelligence agencies when he takes to the stand in New York tomorrow" />
      </a>
      <p>
        
        Abu Hamza argues that he was an intermediary for British intelligence forces trying 'to keep the streets of London safe' when he takes the stand in New York tomorrow.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first gr3ox">
    <a class="http://dailym.ai/RshdBS| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622735-1D1BCAB200000578-221_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="sciencetech item html_snippet_module">
    <div class="article article-tri-headline ">
  <h2 class="linkro-darkred"><a href="#">{{headline86}}</a></h2>
  <div class="articletext">
  <a href="/sciencetech/article-2623421/Now-fly-like-BIRD-Flapping-Oculus-Rift-machine-makes-humans-feel-soaring-skies.html">
  <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/birdflapping.gif" scrolling="no" width="636" frameborder="0" height="400" ></img></a>
  <div><p>Developed by the Zurich University of the Arts in Switzerland, the Birdly translates hand movements from simulator into the flapping of virtual avian wings. Meanwhile, an Oculus Rift VR headset provides a stomach-churning bird-eye-view of the flight. If that wasn't enough, the system also replicates the headwinds that a red kite would face using a fan. Users will even smell whatever landscape they're flying over.</p></div>
  </div>
  <div class="article-icon-links-container">
  <ul class="article-icon-links cleared">
  <li class="first">
  <a class="comments-link" href="/sciencetech/article-2623421/Now-fly-like-BIRD-Flapping-Oculus-Rift-machine-makes-humans-feel-soaring-skies.html#comments" rel="nofollow">
  <span class="icon"></span><span class="linktext">Comments</span>
  </a></li>
  <li class="">
  <a class="videos-link" href="/sciencetech/article-2623421/Now-fly-like-BIRD-Flapping-Oculus-Rift-machine-makes-humans-feel-soaring-skies.html#video" rel="nofollow">
  <span class="icon"></span><span class="linktext">Videos</span>
  </a></li>
  <li class=" gr3ox">
  <a class="http://bit.ly/Za9GE6| js-sl share-link" href="#">
  <span class="icon"></span> <span class="linktext">Share</span>
  </a></li>
  </ul>
  </div>
  </div>
  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline87}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623169/Is-Radio-4-putting-robins-wrong-flightpath-Birds-magnetic-compass-fails-exposed-AM-radio.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623169-1DAA126B00000578-110_154x115.jpg" height="84" width="112" alt="Lost in music: Biologists have proved that the electromagnetic 'noise' from AM radio transmitters interferes with the Earth's magnetic field, which migratory birds such as robins (pictured) use to navigate" />
      </a>
      <p>
        
        Scientists from the University of Oldenburg, Germany, said the problem of electromagnetic noise from AM radio transmitters affects migratory birds in urban areas.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623169/Is-Radio-4-putting-robins-wrong-flightpath-Birds-magnetic-compass-fails-exposed-AM-radio.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623169">          46</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtTAJb| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623169-1DAA126B00000578-327_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline88}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623179/New-30million-golf-resort-built-site-Lord-Beaverbrooks-estate-plans-given-green-light-court-ruling.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623179-1DAA30BE00000578-513_154x115.jpg" height="84" width="112" alt="Grandeur:  Cherkley Court near Leatherhead in Surrey, will now become a luxury golf resort after a High Court decision was overturned on appeal. It is the former estate of media baron and politician Lord Beaverbrook" />
      </a>
      <p>
        
        The plans for Cherkley Court near Leatherhead, Surrey, were scrapped when a High Court judge quashed planning permission in August.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623179/New-30million-golf-resort-built-site-Lord-Beaverbrooks-estate-plans-given-green-light-court-ruling.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623179">           9</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEYXUq| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623179-1DAA30BE00000578-335_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline89}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623039/Andrea-Cristina-Zamfir-crucified-prostitute-stripped-naked-Italy-shown-picture-police-fear-victim-new-Monster-Florence.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623039-1D9E86FD00000578-95_154x115.jpg" height="84" width="112" alt="Murdered: Andrea Cristina Zamfir, 26, was found naked and bound with tape to an iron bar in a position similar to crucifixion, beneath a bridge in Ugnano, a village near Florence, Italy" />
      </a>
      <p>
        
        Andrea Cristina Zamfir was discovered bound with tape to an iron bar in a position similar to crucifixion beneath a bridge in Ugnano, a village near Florence, Italy. She was murdered on Sunday night.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623039/Andrea-Cristina-Zamfir-crucified-prostitute-stripped-naked-Italy-shown-picture-police-fear-victim-new-Monster-Florence.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623039">          48</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEm954| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623039-1DA94BE900000578-438_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline90}}</a>
    </h2>
    <div class="articletext">
      <a href="/femail/article-2623256/David-Beckham-Prince-George-luxury-brands-helping-hand-Britishness-cited-reason-buy-global-shoppers.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAAA25800000578-123_154x115.jpg" height="84" width="112" alt="british" />
      </a>
      <p>
        
        A survey of Chinese consumers who travel thousands of miles to the UK to shop cited 'Britishness' as one of the main reasons.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="Femail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/femail/article-2623256/David-Beckham-Prince-George-luxury-brands-helping-hand-Britishness-cited-reason-buy-global-shoppers.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623256">          43</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru29Uw| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAAA25800000578-810_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline91}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623377/Jury-sworn-Rolf-Harris-child-sex-abuse-trial-prosecution-set-begin-tomorrow.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623377-1DAA194A00000578-312_154x115.jpg" height="84" width="112" alt="Rolf Harris arriving with his wife and daughter at Southwark Crown Court in  London, Thursday, 8th May 2014. Picture by Stephen Lock / i-Images" />
      </a>
      <p>
        
        The 84-year-old, from Bray in Berkshire, appeared at London’s Southwark Crown Court today, accompanied by his wife Alwen.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first gr3ox">
    <a class="http://dailym.ai/RuxRkq| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623377-1DAB804A00000578-84_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline92}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2622635/Crippling-childcare-costs-stopping-135-000-mothers-going-work-claims-Labour.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-0-19E6322300000578-693_154x115.jpg" height="84" width="112" alt="Childcare costs are soaring - leaving many parents unable to return to work, even if they want to" />
      </a>
      <p>
        
        Shadow children's minister Lucy Powell said Ed Miliband's proposal to extend free childcare would allow squeezed families to take on more hours.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2622635/Crippling-childcare-costs-stopping-135-000-mothers-going-work-claims-Labour.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622635">         130</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RrZyug| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/07/article-0-19E6322300000578-958_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline93}}</a>
    </h2>
    <div class="articletext">
        <a href="/health/article-2623229/Soldier-buys-Bosnian-boy-new-100-000-FACE-moved-terrible-facial-deformities.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623229-1DAAB77100000578-560_636x382.jpg" height="382" width="636" alt="Wayne Ingram and Stefan Savic" />
        </a>
      <div >
       <p>
         
         Former Staff Sergeant Wayne Ingram, 44, from Dorset, met Stefan Savic, now 14, a decade ago while on peacekeeping duties in Eastern Europe (left). He was shocked by the facial deformity that Stefan had been born with (inset) and promised to raise enough money for him to have reconstructive surgery at Great Ormond Street Hospital, in London. After tireless fundraising and numerous procedures, his transformation is now almost complete (right).
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/health/article-2623229/Soldier-buys-Bosnian-boy-new-100-000-FACE-moved-terrible-facial-deformities.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623229">         603</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtXSAr| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623229-1DAAB77100000578-560_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline94}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623248/Sprawling-2-000-acre-property-racehorse-breeder-Vernon-Football-Pools-magnate-Robert-Sangster-comes-horse-training-centre-seven-gallops.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623248-1DA9D21E00000578-388_154x115.jpg" height="84" width="112" alt="In a statement, Guy and Ben Sangster, said: 'While it is sad that the family are selling Manton after 30 years of ownership, we are all in agreement that now is the time for another chapter in the illustrious history of this estate'" />
      </a>
      <p>
        
        The 2,000-acre Manton estate near Marlborough, Wiltshire, boasts a 200-year-old manor house and its own hamlet of 24 cottages and 10 flats.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623248/Sprawling-2-000-acre-property-racehorse-breeder-Vernon-Football-Pools-magnate-Robert-Sangster-comes-horse-training-centre-seven-gallops.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623248">         138</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru11jI| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623248-1DA9D21E00000578-261_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline95}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623298/Now-thats-cuff-Contactless-payment-SUIT-lets-pay-shopping-simple-wave-sleeve.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623298-1DAA017000000578-727_154x115.jpg" height="84" width="112" alt="Menswear label M.J. Bale, Heritage Bank and Visa have teamed up to create the suit with a contactless payment chip and antenna woven into the sleeve. The power suit will let men pay 'invisibly' wherever Visa payWave is accepted" />
      </a>
      <p>
        
        Australian tailors have unveiled their 'James Bond' styled suit. It has a contactless payment chip and an antenna built into the sleeve.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623298/Now-thats-cuff-Contactless-payment-SUIT-lets-pay-shopping-simple-wave-sleeve.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623298">          24</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/sciencetech/article-2623298/Now-thats-cuff-Contactless-payment-SUIT-lets-pay-shopping-simple-wave-sleeve.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Rug3WC| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623298-1DAB330F00000578-562_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline96}}</a>
    </h2>
    <div class="articletext">
      <a href="/travel/article-2623153/Women-pack-36-items-EIGHT-pairs-shoes-week-away-91-admit-not-wearing-clothes-holiday.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623153-1DA9F1C900000578-250_154x115.jpg" height="84" width="112" alt="Overpacking: 91 per cent of women admit to not wearing everything they cram into a suitcase" />
      </a>
      <p>
        
        Women are the biggest culprits when it comes to overpacking, with 53 per cent confessing to going over personal baggage allowance in the past five years.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="travelmail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/travel/article-2623153/Women-pack-36-items-EIGHT-pairs-shoes-week-away-91-admit-not-wearing-clothes-holiday.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623153">          30</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://www.dailymail.co.uk/travel/article-2623153/Women-pack-36-items-EIGHT-pairs-shoes-week-away-91-admit-not-wearing-clothes-holiday.html| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623153-1DA9F1C900000578-387_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline97}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623327/The-sun-inside-LIGHT-BULB-17-smart-LED-helps-sleep-mimicking-changing-light-day-night.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623327-1DAB061F00000578-477_154x115.jpg" height="84" width="112" alt="The Drift Light comes with three modes. In Daylight mode, the switch is used in the same way as a standard light. To activate Midnight mode, users flick the switch twice and the bulb fades to dark gradually. By flicking the switch three times, the bulb activates Moonlight mode and fade to low light in 37 minutes" />
      </a>
      <p>
        
        The Drift Light, created in Utah, costs $29 (£17) and reduces the amount of blue light emitted. It gradually fades to mimic sunset and help people sleep better.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623327/The-sun-inside-LIGHT-BULB-17-smart-LED-helps-sleep-mimicking-changing-light-day-night.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623327">           5</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/sciencetech/article-2623327/The-sun-inside-LIGHT-BULB-17-smart-LED-helps-sleep-mimicking-changing-light-day-night.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFxLou| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623327-1DAB061F00000578-328_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline98}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623518/Turning-new-leaf-Italian-prisoners-sentences-reduced-three-days-book-read-jail.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623518-1DAD62AB00000578-714_154x115.jpg" height="84" width="112" alt="Turning over a new leaf: British jails may have banned books for inmates but in Italy, the more prisoners read the more time have knocked off their sentence (file picture)" />
      </a>
      <p>
        
        New legislation set to be passed means that for every book a prisoner gets through, three days will be knocked off their sentence - up to a maximum of 48 days in a year.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623518/Turning-new-leaf-Italian-prisoners-sentences-reduced-three-days-book-read-jail.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623518">           0</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuUMw3| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623518-1DAD62AB00000578-715_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline99}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623299/Archaeologists-5-600-year-old-tomb-mummy-PREDATING-First-Dynasty-pharaohs.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA56F1400000578-136_154x115.jpg" height="84" width="112" alt="Treasure trove: Archaeologists in southern Egypt found a mummy that predates the First Dynasty and the unification of Egypt together with an array of precious objects (pictured), the Egyptian Antiquities Ministry announced" />
      </a>
      <p>
        
        The Egyptian Antiquities Ministry announced the discovery of the tomb in the ancient city of Hierakonpolis located between Luxor and Aswan.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623299/Archaeologists-5-600-year-old-tomb-mummy-PREDATING-First-Dynasty-pharaohs.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623299">          18</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RudLqu| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA56F1400000578-863_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline100}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623450/Chinese-spray-water-2-000-feet-air-dispel-smog.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623450-1DAD0DAB00000578-588_636x382.jpg" height="382" width="636" alt="Now THAT'S a water cannon: Chinese city unveils mega spray that will squirt smog and pollution out of the sky" />
        </a>
      <div >
       <p>
         
         Long-range sprayers have been set up in Lanzhou, capital of China's Gansu province, which will throw out tap water to dispel air pollution. The two long-range sprayers are able to pulverize and spurt out tap water to wipe out dust and smog within a radius of 2,000 feet to reduce air pollution caused by the metro construction.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623450/Chinese-spray-water-2-000-feet-air-dispel-smog.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623450">          22</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuMxjn| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623450-1DAD0DAB00000578-588_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline101}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623164/BREAKING-NEWS-Colin-Pillinger-scientist-Britains-Beagle-Mars-2-mission-dies-aged-70.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA9EEA600000578-638_154x115.jpg" height="84" width="112" alt="Professor Colin Pillinger, lead of the mission to land a British spacecraft on Mars called Beagle 2, has died at the age of 70" />
      </a>
      <p>
        
        Professor Pillinger has died after suffering a brain haemorrhage at his home in Cambridge. The famous planetary scientist had a long and fruitful career.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623164/BREAKING-NEWS-Colin-Pillinger-scientist-Britains-Beagle-Mars-2-mission-dies-aged-70.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623164">          83</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEVvJd| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623164-1DACD6EA00000578-927_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline102}}</a>
    </h2>
    <div class="articletext">
      <a href="/health/article-2623273/Motorbike-accident-causes-mans-heart-SPIN-chest.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623273-1DAAEC1000000578-136_154x115.jpg" height="84" width="112" alt="Doctors in Italy were amazed when a motorbike crash caused a man's heart to rotate 90 degrees to the right. X-ray (left) shows the heart after it had rotated and (right) shows it back in its normal position 24 hours later" />
      </a>
      <p>
        
        Scans showed it had rotated 90 degrees to the right, say University of Padua doctors. The movement may have been caused by air build up in the chest.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/health/article-2623273/Motorbike-accident-causes-mans-heart-SPIN-chest.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623273">           7</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuiqsA| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623273-1DAAEC1000000578-15_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline103}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623158/Police-threaten-strike-Brazil-World-Cup-latest-24-hour-walkout-pay.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623158-1DA5A9A700000578-744_154x115.jpg" height="84" width="112" alt="Federal police protesting for better pay and working conditions while on strike in Rio de Janeiro" />
      </a>
      <p>
        
        Officers staged a protest rally yesterday over pay and working conditions at the Rio de Janeiro concert hall, where national team head coach Luiz Felipe Scolari was announcing his squad for the tournament.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623158/Police-threaten-strike-Brazil-World-Cup-latest-24-hour-walkout-pay.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623158">           9</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mETPPU| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623158-1DAA82F000000578-336_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline104}}</a>
    </h2>
    <div class="articletext">
      <a href="/travel/article-2623380/Why-women-DONT-sunbathe-TWICE-likely-die-women-do.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623380-0646E121000005DC-726_154x115.jpg" height="84" width="112" alt="Could sunbathing be good for us? Researchers say guidelines advising us to stay out of the sun may be harmful" />
      </a>
      <p>
        
        A new study has shown that women who avoid sunbathing during the summer are twice as likely to die than those who sunbathe everyday.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="travelmail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/travel/article-2623380/Why-women-DONT-sunbathe-TWICE-likely-die-women-do.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623380">          69</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuyXwH| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623380-0646E121000005DC-513_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline105}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623368/Married-At-First-Sight-Channel-4-launches-bizarre-idea-marry-two-strangers-reality-show.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623368-1DAA915000000578-423_154x115.jpg" height="84" width="112" alt="Wedding: Six singletons are going to be introduced at the altar and immediately married off on TV" />
      </a>
      <p>
        
        The show, which has a working title of Married At First Sight, will see the couples take part in an experiment to find out if science can produce a stable marriage.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623368/Married-At-First-Sight-Channel-4-launches-bizarre-idea-marry-two-strangers-reality-show.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623368">          94</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuvNZP| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623368-1DAA915000000578-118_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline106}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623143/Watch-footage-captured-police-officers-beat.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623143-1DA9DC4300000578-809_154x115.jpg" height="84" width="112" alt="Dramatic: One of the two videos shows a crying domestic abuse victim with blood all over her chest" />
      </a>
      <p>
        
        WARNING: GRAPHIC CONTENT -- One of the two videos filmed in London shows a crying domestic abuse victim with blood all over her chest.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623143/Watch-footage-captured-police-officers-beat.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623143">         186</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623143/Watch-footage-captured-police-officers-beat.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEQKPY| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623143-1DAA1A0700000578-372_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline107}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2622809/Mother-strangled-two-babies-death-suffering-postnatal-depression-returns-1-5m-mansion-Nappy-valley-two-years-later-release-mental-hospital.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622809-1DAB035600000578-190_636x392.jpg" height="392" width="636" alt="mum" />
        </a>
      <div >
       <p>
         
         Jewellery designer Felicia Boots suffocated her ten-week-old son Mason and 14-month-old daughter Lily (both left) days after the family had moved into a new £1.5m home (inset) in Wandsworth, south west London, in May 2012. Following the tragedy, she was spared jail and was instead detained in a psychiatric hospital until doctors deemed her fit for release. At the time, a judge said a prison sentence would be 'wholly inappropriate'. Now, nearly two years later, she has been spotted walking a dog with her husband Jeff (centre) in the neighbourhood, dubbed 'Nappy Valley'.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2622809/Mother-strangled-two-babies-death-suffering-postnatal-depression-returns-1-5m-mansion-Nappy-valley-two-years-later-release-mental-hospital.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622809">         710</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2622809/Mother-strangled-two-babies-death-suffering-postnatal-depression-returns-1-5m-mansion-Nappy-valley-two-years-later-release-mental-hospital.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RsvaQr| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622809-1DA9AAE100000578-724_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline108}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623332/Pro-Russian-separatists-defy-Putins-plea-call-referendum-seceding-Ukraine-vow-ahead-anyway.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623332-1DAA61E500000578-23_154x115.jpg" height="84" width="112" alt="Change of heart: Putin, pictured during a wreath laying ceremony at the Kremlin, said that a referendum in eastern Ukraine should be postponed" />
      </a>
      <p>
        
        Denis Pushilin, a leader of the self-declared separatist Donetsk People's Republic, said that the 'People's Council' had voted to hold the plebiscite as planned.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623332/Pro-Russian-separatists-defy-Putins-plea-call-referendum-seceding-Ukraine-vow-ahead-anyway.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623332">          10</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623332/Pro-Russian-separatists-defy-Putins-plea-call-referendum-seceding-Ukraine-vow-ahead-anyway.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RulqVC| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623332-1DAA61E500000578-666_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline109}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623178/Shocking-moment-FIVE-daredevil-parachutists-jumped-200ft-church-spire-landing-tiny-market-place.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623178-1DAAA7A300000578-855_154x115.jpg" height="84" width="112" alt="Newark" />
      </a>
      <p>
        
        The mystery group filmed themselves jumping from the spire of Newark Parish Church, Nottinghamshire (left) in the middle of the night.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623178/Shocking-moment-FIVE-daredevil-parachutists-jumped-200ft-church-spire-landing-tiny-market-place.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623178">          36</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623178/Shocking-moment-FIVE-daredevil-parachutists-jumped-200ft-church-spire-landing-tiny-market-place.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEYQIr| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623178-1DAAA7A300000578-681_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline110}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623570/Is-Google-jetpack-coming-Firm-admits-worked-design-says-technology-not-ready-YET.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623570-0B2964A2000005DC-109_154x115.jpg" height="84" width="112" alt="Microsoft recently flew a Jetpack in London to launch its Halo game - but Google says consumer version s are still a long time off" />
      </a>
      <p>
        
        The head of Google's secretive X Labs said the project was on hold until the technology needed catches up.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623570/Is-Google-jetpack-coming-Firm-admits-worked-design-says-technology-not-ready-YET.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623570">           0</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Rv9B1v| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623570-0B2964A2000005DC-964_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline111}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623107/Head-South-Korean-ferry-company-vessel-overturned-killing-300-people-detained-suspicion-knowing-ship-overloaded.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623107-1D70213B00000578-58_154x115.jpg" height="84" width="112" alt="Kim Han-sik, centre, the CEO of the operator of the sunken Sewol, who has been detained by authorities ahead of a possible formal arrest" />
      </a>
      <p>
        
        Kim Han-sik, president of Chonghaejin was detained ahead of his possible formal arrest on allegations that he was aware the ferry exceeded its cargo limit.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623107/Head-South-Korean-ferry-company-vessel-overturned-killing-300-people-detained-suspicion-knowing-ship-overloaded.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623107">           4</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtFjwf| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623107-1D70213B00000578-981_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-large cleared">
    <h2 class="linkro-darkred"><a href="#">{{headline112}}</a>
    </h2>
    <a href="/news/article-2623415/A-peace-history-Buddha-statue-2-000-years-old-raises-two-fingers-just-like-modern-day-anti-war-sign.html">
        <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623415-1DAA086200000578-406_308x395.jpg" height="395" width="308" alt="Pass the incense, man: The 'peace' Buddha" />
    </a>
    <div class="articletext-holder">
      <p>
        
        The 24ft-tall Amita Buddha, located in the 104th cave of the famous Longmen Grottoes in Henan Province, appears to be posing with two fingers raised. It is one of an estimated 100,000 statues of the Buddha and his disciples carved into the living rock of the 1,400 caves at Longmen, which date back nearly 2,000 years. That would make is far older than the peace sign, which was first popularised as 'V for victory' in Europe during the Second World War, but then reversed in meaning by the peace movement in the U.S. during the 1960s.
      </p>
      <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623415/A-peace-history-Buddha-statue-2-000-years-old-raises-two-fingers-just-like-modern-day-anti-war-sign.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623415">          15</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFYRMh| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623415-1DAA086200000578-364_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

    </div>
  </div>


    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline113}}</a>
    </h2>
    <div class="articletext">
        <a href="/health/article-2623372/Google-Glass-enters-operating-theatre-Surgeon-UK-use-smart-specs-operation.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623372-1DAB241E00000578-999_636x390.jpg" height="390" width="636" alt="Since Mr Isaac (right) carried out an operation wearing the glasses other surgeons at the hospital have also tried them. The hospital says they could be a fantastic teaching tool as they allow operations to be filmed meaning students can see surgery from the surgeon's perspective" />
        </a>
      <div >
       <p>
         
         David Isaac, an orthopaedic surgeon at Torbay Hospital in Devon, says many other surgeons at the hospital have followed suit. They say the devices can allow them to live-stream operations to lecture theatres to help train medical students.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/health/article-2623372/Google-Glass-enters-operating-theatre-Surgeon-UK-use-smart-specs-operation.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623372">           4</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFRYun| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623372-1DAB240600000578-930_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline114}}</a>
    </h2>
    <div class="articletext">
      <a href="/femail/article-2622500/Artist-paints-intricate-scenes-eyelids-using-amazing-skill-promote-themes-anti-bullying.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622500-1DAA443B00000578-174_154x115.jpg" height="84" width="112" alt="Tal Peleg Art" />
      </a>
      <p>
        
        A young make-up artist who continues to amaze the art world with her incredible miniature masterpieces - has started creating scenes depicting serious issues.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="Femail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/femail/article-2622500/Artist-paints-intricate-scenes-eyelids-using-amazing-skill-promote-themes-anti-bullying.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622500">          17</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFhH65| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622500-1DAA443B00000578-236_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline115}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623231/Is-real-life-Her-Army-veteran-wants-MARRY-laptop-says-computers-preferred-sexual-object.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623231-1DAA102500000578-514_154x115.jpg" height="84" width="112" alt="Comparison: Sevier's situation is similar to the film Her, where a man, played by Joaquin Phoenix, falls in love with his operating system" />
      </a>
      <p>
        
        Chris Sevier, 36, has filed a 50-page motion to the 10th US Circuit Court of Appeal claiming if same-sex couples are allowed to wed, he should be able to tie the knot with his Macbook, which he claims is laden with pornography.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623231/Is-real-life-Her-Army-veteran-wants-MARRY-laptop-says-computers-preferred-sexual-object.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623231">          55</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtXTEy| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623231-1DAA852600000578-794_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline116}}</a>
    </h2>
    <div class="articletext">
      <a href="/travel/article-2623263/Middle-Eastern-tourists-biggest-spenders-Britain.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623263-1DAACDEE00000578-885_154x115.jpg" height="84" width="112" alt="Big spenders: Visitors from the Middle East and UAE spend the most per day when they in the UK" />
      </a>
      <p>
        
        Britain may welcome more European and American visitors than from any other nation, but the biggest spenders by far are from the Middle East.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="travelmail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/travel/article-2623263/Middle-Eastern-tourists-biggest-spenders-Britain.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623263">          20</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mFhfVz| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623263-1DAACDEE00000578-974_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline117}}</a>
    </h2>
    <div class="articletext">
      <a href="/travel/article-2623235/London-welcomes-tourists-record-breaking-16-8-MILLION-flock-capital.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAA6CAC00000578-939_154x115.jpg" height="84" width="112" alt="London calling: The capital welcome nearly 17 million visitors for the first time in its history" />
      </a>
      <p>
        
        The Olympic Games legacy and a host of blockbuster exhibitions were credited with helping create the bumper tourism year.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="travelmail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/travel/article-2623235/London-welcomes-tourists-record-breaking-16-8-MILLION-flock-capital.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623235">          39</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mF7x5B| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAA6CAC00000578-621_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline118}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2623250/Now-THATs-power-plant-Solar-tree-charges-mobile-gadgets.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DAA06CE00000578-9_154x115.jpg" height="84" width="112" alt="Sun worshiper: The device has nine solar cells which can be swivelled on the 'potplant's' plastic branches to get maximum exposure in the sunlight" />
      </a>
      <p>
        
        A designer from Metz, France came up with the 'plant' which has nine solar cell 'leaves' to charge batteries and USB devices as well as function as a light.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2623250/Now-THATs-power-plant-Solar-tree-charges-mobile-gadgets.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623250">          12</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/sciencetech/article-2623250/Now-THATs-power-plant-Solar-tree-charges-mobile-gadgets.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mF9y1q| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623250-1DAAFC2200000578-275_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline119}}</a>
    </h2>
    <div class="articletext">
      <a href="/travel/article-2623292/Chinese-tourists-flock-pigs-taught-DIVE.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623292-1DAAAB1B00000578-365_154x115.jpg" height="84" width="112" alt="Taking the plunge: The pigs didn't like going in the water initially but soon learnt to enjoy diving" />
      </a>
      <p>
        
        What started as a crazy idea by one pig farmer to keep his animals entertained has now turned into a tourist attraction in China.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="travelmail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/travel/article-2623292/Chinese-tourists-flock-pigs-taught-DIVE.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623292">          26</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://www.dailymail.co.uk/travel/article-2623292/Chinese-tourists-flock-pigs-taught-DIVE.html| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623292-1DAAAB1B00000578-31_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="femail item html_snippet_module">
    <div data-path="http://www.dailymail.co.uk/apps/fffhub/public" class="fff-hub-data"></div><!--[if lt IE 9]><div class="fff-module-include lt-ie9"><![endif]--><!--[if gt IE 8]> <!--><div class="fff-module-include"><!-- <![endif]--><div class="fff-hub"><div style="display:none" class="fff-adblocker-msg"><h5>You appear to have an ad-blocker running which will prevent this page from functioning as intended. Please disable your ad-blocker or set an exception for this page.</h5></div><div class="fff-hottest fff-gall-step-0"><div class="fff-module-title"><h3 class="fff-hottest-header">Today's hottest<span>fashion finds</span></h3><div class="fff-gallery-ui-wrap">See more<div class="fff-hub-arrow fff-hub-left-arrow"></div><div class="fff-hub-arrow fff-hub-right-arrow"></div></div></div><div><div class="fff-hottest-list"><ul><li data-fff-overlay-url="http://i.dailymail.co.uk/i/pix/2014/01/26/article-2546221-1AFA353C00000578-413_634x1179.jpg" data-fff-overlay-productid='98803' data-fff-score='0'><div><h4>Sarah</h4><div class="fff-hottest-hightlight"><div class="fff-hot-celeb"><img src="http://i.dailymail.co.uk/i/pix/2014/01/26/article-2546221-1AFA353C00000578-413_634x1179.jpg" style="width:220px;margin-left:-50px;margin-top:-9px;min-height:411px;"/></div><div class="fff-hottest-product fff-product-wrapper"><div class="fff-circle-img-wrap"><img src="http://www.boohoo.com/content/ebiz/boohoo/invt/azz42829/azz42829_teal_xl.jpg" onerror="this.className+=' imageError';$(this).trigger('product:error');"/></div></div></div><p>Inject some red carpet glamour to your wardrobe</p></div><a class="read_more">Read more &rsaquo;</a></li><li data-fff-overlay-url="http://i.dailymail.co.uk/i/pix/2014/01/10/article-2537390-1A8CA38800000578-778_306x643.jpg" data-fff-overlay-productid='128227' data-fff-score='0'><div><h4>Millie</h4><div class="fff-hottest-hightlight"><div class="fff-hot-celeb"><img src="http://i.dailymail.co.uk/i/pix/2014/01/10/article-2537390-1A8CA38800000578-778_306x643.jpg" style="width:194px;margin-left:-25px;margin-top:0px;min-height:402px;"/></div><div class="fff-hottest-product fff-product-wrapper"><div class="fff-circle-img-wrap"><img src="http://images.asos-media.com/inv/media/7/4/2/6/3166247/image3xl.jpg" onerror="this.className+=' imageError';$(this).trigger('product:error');"/></div></div></div><p>Make like Millie in a military coat by Sandro</p></div><a class="read_more">Read more &rsaquo;</a></li><li data-fff-overlay-url="http://i.dailymail.co.uk/i/pix/2014/01/21/article-2543184-1A975BA400000578-906_634x1181.jpg" data-fff-overlay-productid='138214' data-fff-score='0'><div><h4>Millie</h4><div class="fff-hottest-hightlight"><div class="fff-hot-celeb"><img src="http://i.dailymail.co.uk/i/pix/2014/01/21/article-2543184-1A975BA400000578-906_634x1181.jpg" style="width:219px;margin-left:-46px;margin-top:0px;min-height:402px;"/></div><div class="fff-hottest-product fff-product-wrapper"><div class="fff-circle-img-wrap"><img src="http://static.missguided.co.uk/media/catalog/product/cache/1/image/355x520/9df78eab33525d08d6e5fb8d27136e95/f/i/fiolena_10.jpg" onerror="this.className+=' imageError';$(this).trigger('product:error');"/></div></div></div><p>Stay warm in a quilted jacket like Millie's</p></div><a class="read_more">Read more &rsaquo;</a></li><li data-fff-overlay-url="http://i.dailymail.co.uk/i/pix/2014/01/21/article-2543184-1A975BA400000578-906_634x1181.jpg" data-fff-overlay-productid='138213' data-fff-score='0'><div><h4>Millie</h4><div class="fff-hottest-hightlight"><div class="fff-hot-celeb"><img src="http://i.dailymail.co.uk/i/pix/2014/01/21/article-2543184-1A975BA400000578-906_634x1181.jpg" style="width:219px;margin-left:-46px;margin-top:0px;min-height:402px;"/></div><div class="fff-hottest-product fff-product-wrapper"><div class="fff-circle-img-wrap"><img src="http://images.asos-media.com/inv/media/4/3/3/2/2992334/black/image1xl.jpg" onerror="this.className+=' imageError';$(this).trigger('product:error');"/></div></div></div><p>Stay warm in a quilted jacket like Millie's</p></div><a class="read_more">Read more &rsaquo;</a></li></ul></div></div></div></div></div>
  </div>

    <div class="femail item html_snippet_module">
    <a href="http://www.dailymail.co.uk/femail/fashionfinder/index.html"><img src="http://i.dailymail.co.uk/i/pix/2014/03/25/140314_fff_hub_puff_light.png"></img></a>
  </div>

    <div class="money item defaultStyle_module">
      <div class="modbl">
      <div class="modbr">
        <div class="modtl">
          <div class="modtr">
            <div class="modSides">
              <h4>
                
              </h4>
              <p>
                
              </p>
              <div class="clear">
                &nbsp;
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>


  </div>

        <div class="beta">
        <div class="item mpu_wrapper">
    <div class="mpu adHolder molads_mpu_middle" id="p-1418">
    <script type="text/javascript">
      adverts.addToArray({type:'300x250', pos:'mpu_middle', adProbe:false, dcopt:true});
    </script>
  </div>
  </div>

        <div class="tvshowbiz item">
    <div class="puff cleared" id="p-1419"
       data-track-module="llg-1000114^puff">
    
    <span class="tl">&nbsp;</span>
    <span class="tr">&nbsp;</span>
    <h3 class="wocc">MORE DON'T MISS</h3>
    <ul class="link-bogr2 linkro-wocc">
      <li>
        <a href="/tvshowbiz/article-2623105/Kourtney-Kardashian-pairs-cream-jacket-T-shirt-skinny-jeans-taping-reality-Los-Angeles.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623105-1DA9C03B00000578-182_154x115.jpg" height="115" width="154" alt="Reality star: Kourtney Kardashian left a studio in Los Angeles on Wednesday after filming for Keeping Up With The Kardashians" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Casual chic: Kourtney Kardashian pairs cream jacket with T-shirt and skinny jeans for taping of reality show in Los Angeles
            </strong>
            Effortlessly chic
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623062/Kendall-Jenner-displays-long-legs-leather-trousers-bundles-multi-coloured-jacket.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623062-1DA98BAE00000578-931_154x115.jpg" height="115" width="154" alt="Kendall Jenner displays her long legs in leather trousers as she bundles up in multi-coloured jacket" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Kendall Jenner displays her long legs in leather trousers as she bundles up in multi-coloured jacket
            </strong>
            Teen is still in the Big Apple after Met Gala
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622986/Kim-Kardashian-reveals-lengthy-post-fears-raising-mixed-race-daughter-North-West.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622986-1DAAB9E600000578-58_154x115.jpg" height="115" width="154" alt="'Racism is still alive': Kim Kardashian reveals her serious side as she blogs about her fears over raising a mixed-race child" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'Racism is still alive': Kim Kardashian reveals her serious side as she blogs about her fears over raising a mixed- race child
            </strong>
            Nori is eight months old
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622998/Have-got-tell-Scarlett-Johansson-enjoys-ice-cream-showing-new-haircut-Paris.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622998-1DAA9E3700000578-764_154x115.jpg" height="115" width="154" alt="SCARLETT JOHANSSON" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Looking swell! Scarlett Johansson enjoys an ice cream while showing off new haircut in Paris and a hint of a baby bump
            </strong>
            There's been much talk since March&nbsp;
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623019/Jennifer-Lopez-puts-long-leggy-thigh-skimming-pink-dress-set-American-Idol.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623019-1DA9634400000578-645_154x115.jpg" height="115" width="154" alt="Jennifer Lopez puts on a long and leggy show in thigh-skimming pink dress on set of American Idol" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Jennifer Lopez puts on a long and leggy show in thigh-skimming pink dress on set of American Idol
            </strong>
            The 44-year-old looked gorgeous
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623046/Liz-Hurley-boyfriend-David-Yarrow-head-dinner-London-wearing-identical-outfits-time-went-town.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623046-1DA967A200000578-82_154x115.jpg" height="115" width="154" alt="Liz Hurley and David go to dinner in London" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            It's date night take two! Liz Hurley and boyfriend David Yarrow dine in London... in almost identical outfits to the last time they went out on the town
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622884/Vanessa-Hudgens-bares-flat-tummy-shes-honoured-teen-pregnancy-prevention-event-alongside-Teen-Moms-Maci-Bookout.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622884-1DA8669D00000578-500_154x115.jpg" height="115" width="154" alt="Vanessa Hudgens bares her flat tummy as she's honoured at teen pregnancy prevention event... alongside Teen Mom's Maci Bookout" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Vanessa Hudgens bares her flat tummy as she's honoured at teen pregnancy prevention event... alongside Teen Mom's Maci Bookout
            </strong>
            Pilates have paid off
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623093/Toni-Collette-puts-worst-foot-forward-ruining-romantic-red-carpet-look-chiffon-sleeveless-leather-pleated-skirt-bizarre-shoe-boots.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623093-1DA9D71B00000578-17_154x115.jpg" height="115" width="154" alt="Fashion fail! Toni Collette puts her worst foot forward, ruining her romantic red carpet look of chiffon sleeveless top and leather pleated skirt with bizarre shoe boots" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Fashion fail! Toni Collette puts her worst foot forward, ruining her romantic red carpet look of chiffon sleeveless top and leather pleated skirt with bizarre shoe boots
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623048/Margot-Robbie-grabs-attention-metallic-mini-skirt-huge-embellished-necklace-Dior-event.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623048-1DA9610C00000578-343_154x115.jpg" height="115" width="154" alt="All that glitters! Margot Robbie grabs attention in metallic mini skirt and huge embellished necklace at Dior event" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            All that glitters! Margot Robbie grabs attention in metallic mini skirt and huge embellished necklace at Dior event
            </strong>
            Making us all green with envy
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622817/Margot-Robbie-wears-low-key-look-morning-eyebrow-raising-Met-Gala-outfit.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622817-1DA84EDB00000578-345_154x115.jpg" height="115" width="154" alt="Margot Robbie wears low-key look the morning after her eyebrow-raising Met Gala outfit" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Back to her chic self! Margot Robbie wears low key look showcasing her slim legs the morning after THAT eyebrow-raising Met Gala outfit
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623096/Amber-Le-Bon-works-masculine-trend-oversized-grey-blazer-Karen-Millen-dinner.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA9B24B00000578-178_154x115.jpg" height="115" width="154" alt="Amber Le Bon works masculine trend in oversized grey blazer while Lilah Parsons shows off her slim legs in vibrant red dress for Karen Millen dinner" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Amber Le Bon works masculine trend in oversized grey blazer while Lilah Parsons shows off her slim legs in vibrant red dress for Karen Millen dinner
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623031/Steven-Spielberg-photobombs-Bruce-Springsteen-wife-The-Boss-gets-sneak-attack-own.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA94D5F00000578-831_154x115.jpg" height="115" width="154" alt="One is a Hollywood icon, the other a rock legend. But it seems neither Steven Spielberg nor Bruce Springsteen is content to relinquish the spotlight." />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Steven Spielberg photobombs Bruce Springsteen and his wife... but The Boss gets him back with a sneak attack of his own
            </strong>
            Hollywood meets rock
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622924/Rachel-Stevens-enjoys-day-baby-Minnie-daughter-Amelie-husband-Alex-Bourne.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622924-1DA882CA00000578-859_154x115.jpg" height="115" width="154" alt="Rachel stevens" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            One big happy family: Rachel Stevens enjoys day out with baby Minnie, daughter Amelie and husband Alex Bourne
            </strong>
            Perfect 2.4
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622975/Helena-Christensen-45-takes-plunge-lacy-bra-bustier-Dior-fashion-show.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA8BCAE00000578-178_154x115.jpg" height="115" width="154" alt="Well she WAS a Victoria's Secret model! Helena Christensen, 45, takes the plunge in a lacy bra bustier at Dior fashion show" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Well she WAS a Victoria's Secret model! Helena Christensen, 45, takes the plunge in a lacy bra bustier at Dior fashion show
            </strong>
            Comfortable taking risks
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623013/Adriana-Lima-displays-slim-pins-skintight-leather-trousers-puts-brave-face-just-five-days-marriage-split.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623013-1DA96E2700000578-60_154x115.jpg" height="115" width="154" alt="Adriana Lima displays her slim pins in skintight leather trousers as she puts on a brave face just five days after marriage split" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Adriana Lima displays her slim pins in skintight leather trousers as she puts on a brave face just five days after marriage split
            </strong>
            Life must go on
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623028/Ashton-Kutcher-looks-bit-weary-need-shave-takes-dogs-walk.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623028-1DA966A800000578-256_154x115.jpg" height="115" width="154" alt="Wait until the baby comes! Expectant father Ashton Kutcher looks a bit weary and in need of a shave as he takes the dogs for a walk" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Wait until the baby comes! Expectant father Ashton Kutcher looks a bit weary and in need of a shave as he takes the dogs for a walk
            </strong>
            Feeling anxious?
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623163/Shes-got-68-year-old-Goldie-Hawn-hits-Beverly-Hills-workout-ready-outfit-shows-sexy-age.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623163-1DAA1D5B00000578-631_154x115.jpg" height="115" width="154" alt="Goldie Hawn" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            She's still got it: Goldie Hawn, 68, hits Beverly Hills in a workout-ready outfit
            </strong>
            Can still lay claim to being one of Hollywood's true beauties
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623004/Under-sea-Anna-Sophia-Robb-Evan-Peters-star-hilarious-spoof-The-Little-Mermaid-inspired-director-Sofia-Coppola.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623004-1DA8461000000578-101_154x115.jpg" height="115" width="154" alt="Ariel and Prince Eric: In a still from the Funny Or Die video, Anna Sophia Robb, 20, and Evan Peters, 28, play the roles of the Little Mermaid and her handsome sailor love in a take on Sofia Coppola's directing style" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Under the sea! Anna Sophia Robb and Evan Peters star in hilarious spoof of The Little Mermaid inspired by director Sofia Coppola
            </strong>
            Carrie Diaries star
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622925/Gisele-Bundchen-kicks-heels-fans-Prophetik-hemp-gown-Rainforest-Alliance-Gala-NYC.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622925-1DA8802700000578-821_154x115.jpg" height="115" width="154" alt="Gisele Bundchen kicks up her heels and fans out her Prophetik hemp gown at Rainforest Alliance Gala in NYC" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Gisele Bundchen kicks up her heels and fans out her Prophetik hemp gown at Rainforest Alliance Gala in NYC
            </strong>
            In grey eco-conscious creation
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622903/Mariah-Carey-puts-eye-popping-display-low-cut-figure-hugging-frock-arrives-David-Letterman-promote-new-album.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622903-1DA8504C00000578-438_154x115.jpg" height="115" width="154" alt="Mariah Carey puts on eye-popping display in low-cut frock as she arrives at David Letterman to promote new album" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Mariah Carey puts on eye-popping display in low-cut, figure-hugging frock as she arrives at David Letterman to promote new album
            </strong>
            On 14th studio album
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623050/Nikki-Reed-wipe-smile-face-enjoys-outing-mom-amid-rumours-shes-moving-marriage-split-hunky-Derek-Hough.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623050-1DA972C800000578-207_154x115.jpg" height="115" width="154" alt="Nikki Reed can't wipe the smile from her face as she enjoys outing with her mom amid rumours she's moving on from  marriage split with hunky Derek Hough" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Nikki Reed can't wipe the smile from her face as she enjoys outing with her mom amid rumours she's moving on from marriage split with hunky Derek Hough
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623055/Avengers-stars-Robert-Downey-Jr-Jeremy-Renner-enjoy-joint-family-vacation-Nashville.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623055-1DA9934100000578-291_154x115.jpg" height="115" width="154" alt="Avengers Assemble! Co-stars Robert Downey Jr and Jeremy Renner enjoy joint family vacation in Nashville" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Avengers Assemble! Co-stars Robert Downey Jr and Jeremy Renner enjoy joint family vacation in Nashville
            </strong>
            Spotted at musical festival and the zoo
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622805/Shes-one-literary-lady-Geri-Halliwell-wears-grey-trouser-suit-visit-book-store-North-London.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622805-1DA702D800000578-122_154x115.jpg" height="115" width="154" alt="Geri" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            She's one literary lady: Geri Halliwell wears grey trouser suit to visit a book store in North London
            </strong>
            Not just a product of popular culture...
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623036/Neighbours-crew-walk-set-fight-improved-working-conditions.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623036-1DA9CC4A00000578-931_154x115.jpg" height="115" width="154" alt="Nightmare on Ramsay Street: Neighbours crew to walk off set in battle for improved working conditions" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Nightmare on Ramsay Street: Neighbours crew to walk off set in battle for improved working conditions
            </strong>
            It's all kicking off Down Under
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623001/Hannibal-star-Hugh-Dancy-pushes-young-son-Cyrus-stroller-walks-family-dog-New-York-City.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623001-1DA8F41500000578-971_154x115.jpg" height="115" width="154" alt="Spring stroll: Hugh Dancy pushed son Cyrus in a stroller as he walked the dog on Wednesday in New York City" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Claire's day off? Hannibal star Hugh Dancy pushes young son Cyrus in a stroller and walks family dog in New York City
            </strong>
            On daddy duty
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622972/Dean-McDermott-picks-anniversary-gifts-Victorias-Secret-wife-Tori-Spelling-amid-reports-hit-yummy-mommy-sons-school-year.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622972-1DA8A73000000578-257_154x115.jpg" height="115" width="154" alt="Dean McDermott picks up anniversary gifts from Victoria's Secret for wife Tori Spelling amid reports he 'hit on yummy mommy' at son's school last year" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Dean McDermott picks up anniversary gifts from Victoria's Secret for wife Tori Spelling amid reports he 'hit on yummy mommy' at son's school last year
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622955/Olivia-Wilde-discusses-new-mom-global-conference-event-three-weeks-giving-birth.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622955-1DA89EC600000578-421_154x115.jpg" height="115" width="154" alt="Moms + Social Change: Brand new mom Olivia Wilde, 30, spoke at the 2nd annual conference in New York City Wednesday" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Wilde about motherhood! Olivia discusses being a new mom at global conference event... less than three weeks after giving birth
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622907/Sandra-Bullock-shows-fit-figure-black-skinny-jeans-keeps-simple-flip-flops-Los-Angeles.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622907-1DA8605000000578-408_154x115.jpg" height="115" width="154" alt="Simple style: Sandra Bullock wore a plain white sweatshirt and black headband on Wednesday while out in Los Angeles" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Sandra Bullock, 49, shows off her enviably slim figure in black skinny jeans as she runs errands in L.A.
            </strong>
            Simple but sexy look
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623069/Daphne-Guinness-ditches-theatrical-garb-HOT-PANTS-fabulous-look-Soho.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA97C6400000578-312_154x115.jpg" height="115" width="154" alt="She's always been known for her whimsical and original style of dressing" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Not so boho now! Daphne Guinness, 46, ditches her theatrical garb for HOT PANTS in a less than fabulous look in New York
            </strong>
            Never one to blend in
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622982/Alessandra-Ambrosio-shows-toned-tanned-tummy-shops-healthy-groceries-Whole-Foods.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622982-1DA88AB900000578-426_154x115.jpg" height="115" width="154" alt="Alessandra" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            So that's how she keeps her supermodel figure! Alessandra Ambrosio flashes toned tummy as she shops for healthy groceries at Whole Foods
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622980/Doting-mother-Sarah-Jessica-Parker-does-school-run-children-getting-glammed-two-different-outfits-New-York-events.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622980-1DA8DDD000000578-710_154x115.jpg" height="115" width="154" alt="Don't know how she does it! Doting mother Sarah Jessica Parker does school run with her children before getting glammed up in two different outfits for New York events" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Don't know how she does it! Doting mother Sarah Jessica Parker does school run with her children before getting glammed up in two different outfits
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622607/A-doctor-opera-singer-tattooed-firefighter-Revealed-The-men-vying-The-Bachelorettes-heart-Will-Andi-Dorfman-true-love-time-around.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622607-1DA867B000000578-878_154x115.jpg" height="115" width="154" alt="bachelorette puff" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            A doctor, an opera singer and a tattooed firefighter: The men vying for Bachelorette's heart. Will Andi Dorfman find true love this time?
            </strong>
            Still looking for love
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623161/Daddys-little-girl-Keith-Urbans-youngest-daughter-surprises-country-singer-cuddle-backstage-American-Idol.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623161-1DAA197E00000578-459_154x115.jpg" height="115" width="154" alt="Keith Urban's youngest daughter makes a surprise visit backstage at American Idol" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Daddy's little girl! Keith Urban's youngest daughter surprises the country singer with a cuddle backstage at American Idol
            </strong>
            Faith is image of mum
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622841/Ellen-Page-steps-bearded-friend-opens-two-ex-girlfriends-hunt-Ms-Right.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622841-1DA72A8E00000578-126_154x115.jpg" height="115" width="154" alt="The odd couple! Ellen Page steps out with bearded friend as she opens up about two ex-girlfriends and her hunt for Ms. Right" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            The odd couple! Ellen Page steps out with bearded friend as she opens up about two ex-girlfriends and her hunt for Ms. Right
            </strong>
            New candid interview
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623014/Got-milk-The-Voice-Australia-causes-social-media-storm-contestants-partner-breastfeeds-live-audition.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623014-1DA905C400000578-359_154x115.jpg" height="115" width="154" alt="'Uncalled for!' The Voice Australia causes a social media storm after contestant's partner breastfeeds during live audition" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'Uncalled for!' The Voice Australia causes a social media storm after contestant's partner breastfeeds during live audition
            </strong>
            Stunned some viewers
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622847/Audrina-Patridge-thrills-mismatched-bikini-frolics-sea-boyfriend-Mexico.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622847-1DA83DA900000578-779_154x115.jpg" height="115" width="154" alt="Audrina" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            The Hills star Audrina Patridge thrills in mismatched bikini as she frolics in sea with boyfriend in Mexico
            </strong>
            With long-term love Corey Bohan
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623021/The-Fault-In-Our-Stars-Shailene-Woodley-dapper-navy-blue-ensemble-white-loafers-cast-reunite.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623021-1DA5810300000578-604_154x115.jpg" height="115" width="154" alt="Fashion forward: Shailene wore a navy blue ensemble by Osman and white Keds shoes while on the set of Despierta America May 7th, seen here with William Valdes" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            The Fault In Our Stars' Shailene Woodley is dapper in navy blue ensemble and white loafers as cast reunite
            </strong>
            Appeared on the set of Despierta America
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622984/Hilaria-Baldwin-sits-Kendall-Kylie-Jenner-talk-big-sister-Kim-Kardashians-wedding.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622984-1DA89ABB00000578-985_154x115.jpg" height="115" width="154" alt="Getting the scoop: Hilaria Baldwin on set of Extra with Kylie and Kendall Jenner, along with Steve Madden, on Wednesday" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'Kimye wedding news!' Extra host Hilaria Baldwin chats with Kendall and Kylie Jenner about big sister Kim's nuptials
            </strong>
            The inside track
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623010/Jackie-Lynn-Taylor-starred-one-The-Little-Rascals-Our-Gang-comedy-shorts-1930s-dies-aged-88.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623010-1DA8D15200000578-902_154x115.jpg" height="115" width="154" alt="Jackie" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Farewell to a Little Rascal: Jackie Lynn Taylor who starred in the Our Gang comedy shorts in the 1930s dies aged 88
            </strong>
            End of an era
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623017/Emma-Roberts-goes-West-Hollywood-shopping-spree-discussing-Aunt-Julias-dirty-mouth-Jimmy-Kimmel-Live.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623017-1DAAE17400000578-623_154x115.jpg" height="115" width="154" alt="Talk show: Emma Roberts opened up about the emotional moment she got pulled over by a police officer while she was driving, during an appearance on Jimmy Kimmel Live on Tuesday night" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'I have to go to court and I'm scared!': Emma Roberts talks tearful moment she got pulled over by police on Jimmy Kimmel Live
            </strong>
            Naughty, not nice...
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622940/Miranda-Kerr-swaps-maxi-dress-tight-jeans-sneakers-checking-Sydney-International-Airport.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622940-1DA8802B00000578-615_154x115.jpg" height="115" width="154" alt="Airport style: Supermodel Miranda Kerr made a quick outfit change after arriving at Sydney International Airport onThursday morning" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Quick change! Miranda Kerr swaps maxi dress for tight jeans and sneakers after checking in at Sydney International Airport
            </strong>
            Long-haul comfort is key
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622886/Jake-Gyllenhaal-smile-face-Alyssa-Miller-spotted-time-reconciliation-February.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622886-1DA71DE400000578-629_154x115.jpg" height="115" width="154" alt="Jake Gyllenhaal can't keep smile off his face as he and Alyssa Miller are spotted together for first time since reconciliation in February" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Jake Gyllenhaal can't keep smile off his face as he and Alyssa Miller are spotted together for first time since reconciliation in February
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622993/Hayden-Christensen-steps-trendy-cardigan-stovepipe-jeans-grabs-lunch-friend.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622993-1DA901B800000578-825_154x115.jpg" height="115" width="154" alt="Attack of the hipster! Hayden Christensen steps out in trendy cardigan and stovepipe jeans as he grabs lunch with a friend" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Attack of the hipster: Hayden Christensen steps out in trendy cardigan and stovepipe jeans as he grabs lunch with a friend
            </strong>
            In Los Angeles
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623011/Denise-Richards-daughters-Sam-Lola-lend-hand-mundane-grocery-shopping-run.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623011-1DA8E88F00000578-849_154x115.jpg" height="115" width="154" alt="Mommy's little helpers: Denise Richards' daughters Sam and Lola turn mundane grocery shopping trip into a fun excursion" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Mommy's little helpers: Denise Richards' daughters Sam and Lola lend a hand during mundane grocery shopping run
            </strong>
            Quite a handful
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622799/Embracing-dark-Kendall-Jenner-takes-night-black-ensemble.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622799-1DA6E2E700000578-73_154x115.jpg" height="115" width="154" alt="Embracing her dark side! Kendall Jenner takes on the night in an all-black ensemble" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Embracing her dark side! Kendall Jenner takes on the night in an all-black ensemble after she gets 'friendly' with Selena Gomez again
            </strong>
            East Coast uniform
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622965/Doutzen-Kroes-cradles-pregnant-belly-elegant-floor-length-gown-charity-event.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622965-1DA879BB00000578-158_154x115.jpg" height="115" width="154" alt="Kroes" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Now THAT'S called maternity chic! Doutzen Kroes cradles her pregnant belly in elegant floor-length gown at charity event
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2622872/Curly-girls-world-unite-lets-end-tyranny-straighteners-says-JILL-FOSTER.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622872-1DA667CF00000578-271_154x115.jpg" height="115" width="154" alt="jill" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Curly girls of the world unite - lets end the tyranny of straighteners! says JILL FOSTER
            </strong>
            Her hair has more twists and turns than an Underground map
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623008/Back-stylish-best-Zoe-Saldana-minimalist-chic-fitted-sweater-dress-fashion-fail-Met-Gala.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA8EF2000000578-396_154x115.jpg" height="115" width="154" alt="Back to her stylish best! Zoe Saldana is minimalist chic in fitted sweater dress after fashion fail at the Met Gala" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Back to her stylish best: Zoe Saldana is minimalist chic in fitted sweater dress after fashion fail at the Met Gala
            </strong>
            Kept it simple
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2622485/The-five-things-hes-thinking-sees-naked-vice-versa-Sex-expert-Tracey-Cox-goes-heads-partners-strip-off.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622485-1DA55C5F00000578-548_154x115.jpg" height="115" width="154" alt="Naked" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            The five things he's thinking when he first sees you naked - and vice versa! Sex expert Tracey Cox on what goes through our heads when partners strip off
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622667/Angelina-Jolie-quite-vixen-long-lost-photoshoot-taken-budding-20-year-old-actress.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622667-1DA6198B00000578-253_154x115.jpg" height="115" width="154" alt="The set of shots show Angelina vamping it up for the camera in feathered jacket and short black mini dress" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            The lady was a vamp! Now-demure Angelina Jolie is quite the vixen in long lost photoshoot taken when she was a budding 20-year-old actress
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622968/Hugh-Jackman-steps-time-interview-himself.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622968-1DA893D600000578-526_154x115.jpg" height="115" width="154" alt="'You are by far the biggest star ever!,' Hugh Jackman travels back to 1999 to tell his younger self what to expect after X-Men" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'You are by far the biggest star ever!' Hugh Jackman travels back to 1999 to tell his younger self what to expect after X-Men
            </strong>
            Life has changed a lot
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622992/Kylie-Minogue-joins-singing-nun-Sister-Cristina-Sister-Act-The-Voice-Italy.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA8A6A400000578-644_154x115.jpg" height="115" width="154" alt="Sister Act: Kylie Minogue performs with Sister Cristina Scuccia on The Voice Italy on Wednesday" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            The hills are alive with the Sound Of Music! Kylie Minogue joins singing nun for a Sister Act on stage for The Voice Italy
            </strong>
            Quite the duet!
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623026/Naomi-Watts-works-sweat-latest-visit-Brentwood-gym-California-stays-looking-cool-catseye-sunnies.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623026-1DA9536A00000578-690_154x115.jpg" height="115" width="154" alt="Naomi Watts is back at the gym after Met Gala" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Keeping fit has never looked so good! Naomi Watts works up a sweat at the gym and stays looking cool in cats eye sunnies
            </strong>
            Working hard on figure
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622936/Myleene-Klass-styles-hair-braided-updo-leaves-ITV-studios-floral-dress.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA8758D00000578-502_154x115.jpg" height="115" width="154" alt="Myleene" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Hey Heidi! Myleene Klass styles her hair into a braided updo as she leaves the ITV studios in a floral dress
            </strong>
            Known for her usually&nbsp; flowing brunette hair
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622863/Jennifer-Lopez-divorce-new-love-twins-helped-grow-human-being.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622863-1DA9812700000578-373_154x115.jpg" height="115" width="154" alt="Lopez" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'I went through a tremendous low': Jennifer Lopez on divorce, new love and how her twins helped her 'grow as a human being'
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622937/Kim-Kardashian-Kanye-Wests-controversial-Vogue-issue-sells-250-000-copies-LESS-expected.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622937-1DA8917600000578-921_154x115.jpg" height="115" width="154" alt="Kim" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            So the risk DIDN'T pay off? Kim Kardashian and Kanye West's controversial Vogue issue 'sells 250,000 copies LESS than expected'
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/news/article-2622952/Its-not-just-sleaze-I-abhor-naked-cynicism-ANNABEL-COLE-took-15-year-old-girl-Miley-Cyruss-British-Heres-verdict.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622952-1DA0458400000578-222_154x115.jpg" height="115" width="154" alt="Crotch-grabbing, grinding and yet more foul language: Miley Cyrus performs at 02 Arena in London" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            It's not just the sleaze I abhor - it's the naked cynicism: ANNABEL COLE took her 15-year -old girl to see Miley Cyrus's British show. Here's her verdict
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622682/Fifty-Shades-Of-Greys-Dakota-Johnson-bares-pale-legs-black-navy-blue-ensemble-stepping-NYC.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622682-1DA6C71900000578-82_154x115.jpg" height="115" width="154" alt="Dakota Johnson" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            No Fifty Shades Of Grey here! Dakota Johnson bares her pale legs in a black and navy blue ensemble stepping out in NYC
            </strong>
            50 Shades of Pale...
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623047/Jordana-Brewster-enjoys-leisurely-shopping-trip-baby-Julian-pregnant-pal.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623047-1DA92ED100000578-759_154x115.jpg" height="115" width="154" alt="Jordana" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Nothing fast or furious going on here! Jordana Brewster enjoys leisurely shopping trip with baby Julian and a pregnant pal
            </strong>
            Doted on her son
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622942/Mary-Kate-Olsen-wraps-elaborate-printed-coat-twin-sister-Ashley-opts-minimalist-chic-skinny-jeans-grey-cardigan-LAX.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622942-1DA885F100000578-946_154x115.jpg" height="115" width="154" alt="Mary-Kate Olsen wraps up in elaborate printed coat while twin sister Ashley opts for minimalist chic in skinny jeans and grey cardigan at LAX" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Mary-Kate Olsen wraps up in elaborate printed coat while twin sister Ashley opts for minimalist chic in skinny jeans and grey cardigan at LAX
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622878/Heavily-pregnant-Kendra-Wilkinson-beams-dressed-lunch-husband-Hank-Baskett.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622878-1DA8619D00000578-340_154x115.jpg" height="115" width="154" alt="Any day now! Heavily pregnant Kendra Wilkinson beams at dressed-down lunch with husband Hank Baskett" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Any day now! Heavily pregnant Kendra Wilkinson beams at dressed-down lunch with husband Hank Baskett
            </strong>
            Due mid-May
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622630/Kim-Kardashian-confirms-wedding-NOT-televised.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622630-1DA6423F00000578-879_154x115.jpg" height="115" width="154" alt="Kim Kardashian confirms wedding will NOT be televised¿ saying (ahem) 'privacy is our main priority'" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Kim confirms wedding will NOT be televised... saying (ahem) 'privacy is our main priority'
            </strong>
            She said: 'You will see everything leading up til and after! (sic)
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622922/Game-Of-Thrones-star-Maisie-Williams-mimics-make-style-New-Zealand-songstress-Lorde.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622922-1DA6F79900000578-905_154x115.jpg" height="115" width="154" alt="Seeing double: Maisie Williams (left) shared this split image of herself next to songstress Lorde on Twitter on Wednesday" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Good Lorde, that's a familiar look! Game Of Thrones star Maisie Williams mimics the make-up style of New Zealand songstress
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622622/Kristin-Cavallari-welcomes-second-son-19-months-time-mother.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622622-1DA7146A00000578-54_154x115.jpg" height="115" width="154" alt="He's arrived! Kristin Cavallari welcomes second son... 21 months after becoming first time mother" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            He's arrived! Kristin Cavallari welcomes second son... 21 months after becoming first time mother
            </strong>
            Ex-Hills star gave birth Jaxon Wyatt on Weds
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622568/Bruce-Willis-father-fifth-time-wife-Emma-Heming-gives-second-child.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622568-1D70A49400000578-663_154x115.jpg" height="115" width="154" alt="Another girl! Bruce Willis becomes father for fifth time as wife Emma Heming gives birth to their second child" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Another girl! Bruce Willis becomes father for fifth time as wife Emma Heming gives birth to their second child
            </strong>
            gave birth in LA
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622429/Katie-Prices-ex-Alex-Reid-offers-support-amid-claims-husband-Kieran-Hayler-cheated-her.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622429-1DA5325B00000578-979_154x115.jpg" height="115" width="154" alt="Alex talks about Katie Price relationship problems" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            EXCLUSIVE - 'She has always struggled with trust issues': Katie Price's ex Alex Reid offers support amid claims that husband Kieran Hayler cheated
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622620/Christine-Bleakley-shows-muscular-arms-sleeveless-peach-ITV-studios.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622620-1DA5EE2700000578-586_154x115.jpg" height="115" width="154" alt="Christine" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Christine Beastly! Ms Bleakley shows off her muscular arms in a sleeveless peach blouse at the ITV studios
            </strong>
            4 years ago said I don't want 'Madonna arms
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622828/Stacy-Keibler-wishes-happiness-ex-George-Clooney-fiancee-revealed-2M-spent-lavish-wedding.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622828-1DA724A900000578-895_154x115.jpg" height="115" width="154" alt="Stacy Keibler 'irked' ex George Clooney proposed to Amal Alamuddin... as it's revealed $2 MILLION will be spent on the lavish Italian wedding" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Stacy Keibler 'wishes nothing but happiness' for ex George Clooney and his fiancee... as it's revealed $2M will be spent on lavish wedding
            </strong>
            Both have moved on
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622733/Georgia-May-Jagger-wears-striped-dress-flip-switch-charity-campaign-Empire-State-Building.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622733-1DA672CF00000578-280_154x115.jpg" height="115" width="154" alt="Georgia May Jagger" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Lighting up the city! Georgia Jagger wears a striped dress to flip the switch for charity campaign at the Empire State Building
            </strong>
            For Delete Blood Cancer
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622858/Bearded-Austrian-drag-queen-splits-opinion-ahead-Eurovision-performance-song-Rise-Like-A-Phoenix.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622858-1DA8452300000578-774_154x115.jpg" height="115" width="154" alt="Bearded Austrian drag queen splits opinion ahead of first Eurovision performance with song Rise Like A Phoenix" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Bearded Austrian drag queen splits opinion ahead of first Eurovision performance with song Rise Like A Phoenix
            </strong>
            And has yet to perform in the semi-final!
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622959/Julianne-Hough-flashes-flesh-black-sports-bra-arrives-Dancing-With-The-Stars-studio.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622959-1DA8905200000578-816_154x115.jpg" height="115" width="154" alt="Loose fit: Julianne Hough flashed some flesh on Wednesday as she arrived at the Dancing With The Stars rehearsal studio in Los Angeles" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            She dares to bare! Julianne Hough flashes toned back and black sports bra as she arrives at Dancing With The Stars studio
            </strong>
            And hat to top it off
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622774/Lana-Del-Rey-sultry-siren-engulfed-flames-moody-new-West-Coast-music-video.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622774-1DA5DA8C00000578-858_154x115.jpg" height="115" width="154" alt="She's on fire! Lana Del Rey is a sultry siren engulfed by flames in her moody new West Coast music video" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            She's on fire! Lana Del Rey is a sultry siren engulfed by flames in her moody new West Coast music video
            </strong>
            Promised it would be 'darker than the first'
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622931/SEBASTIAN-SHAKESPEARE-Mr-Winslets-aristocratic-ex-wife-turns-Hinduism.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622931-013AC56D000004B0-136_154x115.jpg" height="115" width="154" alt="Publishing heiress Eliza Pearson, 25, pictured with her boyfriend Leif Christian Kvaal, has named her first child Anokhi Jaya" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            SEBASTIAN SHAKESPEARE: Mr Winslet's aristocratic ex-wife turns to Hinduism
            </strong>
            Eliza Pearson, 25, has named child Anokhi Jaya
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622862/Beautiful-Marion-Cotillard-effortlessly-gorgeous-pink-shift-dress-chic-shoe-boots.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622862-1DA8C99600000578-496_154x115.jpg" height="115" width="154" alt="Natural beauty: Oscar winner Marion Cotillard looked typically gorgeous on Wednesday at a Dior fashion show in New York City" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            French fancy! Beautiful Marion Cotillard is effortlessly gorgeous in pink shift dress and chic shoe boots
            </strong>
            Left New Yorkers in the shade on Wednesday&nbsp;
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622593/Neil-Patrick-Harris-poses-nude-Rolling-Stone-cover-perfectly-placed-headgear-protecting-modesty.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622593-1DA5DEBA00000578-108_154x115.jpg" height="115" width="154" alt="Neil Patrick Harris poses nude on Rolling Stone cover... with just some perfectly placed headgear protecting his modesty" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            You can leave your hat on! Neil Patrick Harris poses nude on Rolling Stone cover... with just some perfectly placed headgear protecting his modesty
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623227/Charlotte-Dawsons-homeware-designs-completed-friends-family.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623227-1DAA810700000578-894_154x115.jpg" height="115" width="154" alt="Friends and family of Charlotte Dawson are releasing a collection of homewares created by the late television personality before her death" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Finishing her final project: Tragic Aussie presenter Charlotte Dawson's collection of homeware designs will be completed by her friends and family
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2622891/How-does-Botox-free-Felicity-Kendal-look-good-67.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622891-1DA6F55B00000578-594_154x115.jpg" height="115" width="154" alt="felicity" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            How does 'Botox free' Felicity Kendal look this good at 67?
            </strong>
            The Good Life's Barbara Good is... still looking good!
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622751/Alex-Jones-wears-pink-trousers-check-World-War-II-tank-needs-help-getting-it.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622751-1DA6D8FF00000578-338_154x115.jpg" height="115" width="154" alt="alex jones" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Alex Jones wears pink trousers to check out a World War II tank... but needs some help getting out of it
            </strong>
            Just as well she didn't have to get into a trench
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2622802/A-living-bereavement-When-ESTHER-RANTZEN-spoke-couples-denied-access-grandchildren-triggered-flood-heart-rending-stories-revealing-agony-family-breakdowns-forgotten-victims.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622802-1DA71D6A00000578-428_154x115.jpg" height="115" width="154" alt="Esther Rantzen, television presenter" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            A living bereavement: When ESTHER RANTZEN spoke up for couples denied access to their grandchildren, she triggered a flood of heart rending stories
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2621475/Kiefer-Sutherland-not-dating-actress-Sofia-Karstens.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2621475-1DA95CA700000578-194_154x115.jpg" height="115" width="154" alt="He's still a bachelor! Kiefer Sutherland denies that he is dating actress Sofia Karstens" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            He's still a bachelor! Kiefer Sutherland denies that he is dating actress Sofia Karstens
            </strong>
            'Been out 'once or twice, but there's nothing more to it.,' says actor's rep
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622989/Youre-supposed-looking-shoes-Australian-glamour-Cheyenne-Tozzi-flashes-hole-lotta-leg-shoot-Wanteds-new-pumps.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622989-1DA8F02000000578-578_154x115.jpg" height="115" width="154" alt="Cheyenne Tozzi photo shoot" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            You're supposed to be looking at the shoes! Australian glamour Cheyenne Tozzi flashes a hole lotta' leg in photo shoot for shoe brand Wanted's new range
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623025/Cheyenne-Tozzi-stocks-green-beans-grocery-shopping-Sydney.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA946DF00000578-787_154x115.jpg" height="115" width="154" alt="Cheyenne Tozzi" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            So THAT'S how she stays trim! Cheyenne Tozzi stocks up on green beans and does dressed down with style while grocery shopping in Sydney
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/news/article-2622410/EXCLUSIVE-Tori-Spellings-new-crisis-She-needs-major-spinal-surgery-refusing-operation-fears-life-Dean-spin-control.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622410-1DA6142500000578-180_154x115.jpg" height="115" width="154" alt="Tori" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            EXCLUSIVE: Tori Spelling's new crisis: She needs major spinal surgery but refuses the operation because 'her life with Dean will spin further out of control'
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622913/Halle-Berry-goes-slacker-slicker-set-new-astronaut-series.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622913-1DA877E700000578-45_154x115.jpg" height="115" width="154" alt="What a transformation! Halle Berry goes from drab to fab in two very different outfits on set of new TV series" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            What a difference some heels make! Halle Berry goes from slacker to slicker on set of new astronaut series
            </strong>
            In a white T-shirt and cut-off cargo trousers
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622958/Karolina-Kurkova-enjoys-rare-downtime-two-leading-men-busy-days-glamming-fashion-set.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622958-1DA8830500000578-855_154x115.jpg" height="115" width="154" alt="Off-duty beauty: Karolina Kurkova enjoys some rare downtime with her two leading men after a busy few days glamming it up with the fashion set" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Off-duty beauty: Karolina Kurkova enjoys some rare downtime with her two leading men after a busy few days glamming it up with the fashion set
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623088/Whats-secret-Jules-Guy-Sebastians-wife-shows-incredible-post-baby-body-just-three-weeks-giving-birth.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623088-1DAA980500000578-868_154x115.jpg" height="115" width="154" alt="There's just no stopping Jules Sebastian.It's been just a matter of weeks since Guy Sebastian's wife gave birth to their second baby, Archer but the stylist and TV presenter couldn't wait to get back to work" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Aussie TV star Guy Sebastian's wife Jules shows off incredible post-baby body just three weeks after giving birth
            </strong>
            Very trim indeed
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2622741/Ivanka-Trump-reveals-transformed-belle-Met-ball-candid-set-scenes-pictures.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622741-1DA65AF800000578-985_154x115.jpg" height="115" width="154" alt="Princess and her prince: Ivanka Trump helped tie husband Jared Kushner''s bow tie, writing, 'The unsung fashion hero of the evening, my handsome husband Jared'" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Ivanka Trump reveals how she transformed into the belle of the Met ball in candid set of behind-the-scenes pictures
            </strong>
            Real family effort
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622715/Ben-Affleck-laughs-card-counting-scandal-spotted-banned-blackjack-Las-Vegas-casino.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622715-1DA6586C00000578-302_154x115.jpg" height="115" width="154" alt="Ben Affleck laughs off card counting scandal as he is spotted after being banned from blackjack at Las Vegas casino" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Ben Affleck laughs off card counting scandal as he is spotted after being banned from blackjack at Las Vegas casino
            </strong>
            Making a gas stop
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2622938/Little-boy-says-went-Heaven-came-Its-gripped-America-Hollywood-film-four-year-olds-startlingly-vivid-account-meeting-God-died-hospital.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622938-1D67D97800000578-414_154x115.jpg" height="115" width="154" alt="Colton Burpo, from Nebraska, U.S, miraculously survived a life-threatening burst appendix in March 2003 and claims to have gone to Heaven and met Jesus while on the operating table" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Little boy who says he went to Heaven - then came back! It's gripped America and become a Hollywood film - a four-year-old's vivid account of meeting God&nbsp;
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622640/Oprah-Winfrey-60-declares-age-just-number-stunning-tight-red-gown.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622640-1DA606C100000578-332_154x115.jpg" height="115" width="154" alt="Having an O moment! Oprah Winfrey, 60, declares age is just a number in a stunning tight red gown" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Having an O moment! Oprah Winfrey, 60, declares age is just a number in a stunning tight red gown
            </strong>
            Looking younger than ever
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622517/London-calling-Lindsay-Lohan-works-demure-blouse-flirty-miniskirt-pull-socks-night-partying.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-0-1DA5662A00000578-347_154x115.jpg" height="115" width="154" alt="Lindsay Lohan was spotted on yet another night out in the English capital, and was seen heading to Hakkasan restaurant in London's Soho" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            London calling! Lindsay Lohan works demure blouse, flirty miniskirt and pull-up socks for another night of partying
            </strong>
            We thought she had calmed down...
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622951/How-Big-Yin-met-Grim-Reaper-got-big-laugh-CHRISTOPHER-STEVENS-reviews-nights-TV.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622951-1D71BB7600000578-697_154x115.jpg" height="115" width="154" alt="In Billy Connolley's Big Send Off he seems so at ease with his future demise, so offhand and accepting, that you feel he must have been subconsciously readying himself for a long time" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            How the Big Yin met the Grim Reaper... and got a big laugh: CHRISTOPHER STEVENS reviews last night's TV
            </strong>
            Every murder needs a mortuary...
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622904/Rebel-Wilson-2014s-Goldie-Hawn-remake-1980s-classic-Private-Benjamin.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622904-1DA878B100000578-435_154x115.jpg" height="115" width="154" alt="Fat Amy joins the army! Rebel Wilson is 2014's Goldie Hawn in remake of 1980's classic Private Benjamin" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Fat Amy joins the army! Rebel Wilson is 2014's Goldie Hawn in remake of 1980's classic Private Benjamin
            </strong>
            Played Fat Amy in 2012's Pitch Perfect
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622575/Rita-Ora-steps-baggy-basketball-jersey-favourite-boots-wearing-VERY-low-cut-leather-dress-dinner-boyfriend-Calvin-Harris.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622575-1DA6394D00000578-477_154x115.jpg" height="115" width="154" alt="What a sport! Rita Ora steps out in baggy basketball jersey and favourite boots... after wearing them with VERY low cut leather dress for dinner with boyfriend Calvin Harris" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            What a sport! Rita Ora steps out in baggy basketball jersey and favourite boots... after wearing them with VERY low cut dress for dinner with Calvin Harris
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2623080/Ruby-Rose-does-ladylike-glamour-covering-tattoos-fianc-e-Phoebe-Dahl.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623080-1DA9B14400000578-928_154x115.jpg" height="115" width="154" alt="Look of love: It was an unusual look for Ruby who we are used to seeing with piercings and tattoos" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Fair ladies! Aussie model Ruby Rose does ladylike glamour by covering up tattoos as she steps out with fiancée Phoebe Dahl
            </strong>
            Loved-up couple
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622670/Former-ER-star-Mekhi-Phifer-files-bankruptcy-debts-totalling-1-3million.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622670-1DA6367B00000578-376_154x115.jpg" height="115" width="154" alt="Former ER star Mekhi Phifer 'files for bankruptcy with debts totalling $1.3million'" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Former ER star Mekhi Phifer 'files for bankruptcy with debts totalling $1.3million'
            </strong>
            And is claiming around $67,000 in assets
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622707/Motherhood-walk-park-Bethenny-Frankel-dotes-Bryn-playdate.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622707-1DA64E8A00000578-755_154x115.jpg" height="115" width="154" alt="Motherhood is a walk in the park for Bethenny Frankel as she dotes over Bryn during a playdate" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Motherhood is a walk in the park for Bethenny Frankel as she dotes over Bryn during a playdate
            </strong>
            Life is still one big picnic for Bethenny
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622706/Tom-Felton-girlfriend-Jade-Olivia-load-car-canine-supplies-head-dog.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622706-1DA61E4000000578-393_154x115.jpg" height="115" width="154" alt="Tom Felton" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            A walk to remember: Tom Felton and his girlfriend Jade Olivia load up their car with canine supplies as they head out with their dog
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622994/J-Lo-blown-away-Jena-Irenes-Elvis-cover-American-Idol-mouths-word-f.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622994-1DA92AAC00000578-776_154x115.jpg" height="115" width="154" alt="Stunning rendition: Jennifer Lopez reacted as American Idol contestant Jena Irene reached incredibly high notes on Wednesday while performing an Elvis Presley song" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            What did she say? J-Lo is so blown away by Jena Irene's Elvis cover on American Idol that she mouths the word 'f***'
            </strong>
            Calm down!
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622548/Michelle-Heaton-tells-Lorraine-time-baby-Aaron-Jay-contracted-viral-meningitis.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622548-1DA59AFD00000578-168_154x115.jpg" height="115" width="154" alt="Michelle Heaton on Lorraine" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'I knew something wasn't right': Michelle Heaton tells Lorraine about the time her baby Aaron Jay contracted viral meningitis in first TV interview
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622619/Amber-Rose-keeps-figure-wraps-baggy-hoodie-takes-Lil-Angel-Sebastian-grocery-shopping.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622619-1DA63D4C00000578-85_154x115.jpg" height="115" width="154" alt="Amber Rose" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Make-up free Amber Rose keeps her figure under wraps in baggy hoodie as she takes her 'Lil Angel' Sebastian grocery shopping
            </strong>
            Unusually shy
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622473/Charlize-Theron-makes-mockery-catwalk-roots-pulling-cringe-worthy-model-faces-new-SNL-promotional-video.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622473-1DA603C900000578-572_154x115.jpg" height="115" width="154" alt="Is THAT how she got discovered? Charlize Theron makes a mockery of her catwalk roots by pulling cringe-worthy 'model faces' in new SNL promotional video" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Is THAT how she got discovered? Charlize Theron makes a mockery of her catwalk roots by pulling cringe-worthy 'model faces' in SNL promotional video
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2622481/Child-abuse-issue-feel-passionate-stopping-Abbey-Clancy-Melinda-Messenger-ambassadors-NSPCC-charity-campaign.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622481-1DA5697E00000578-74_154x115.jpg" height="115" width="154" alt="abbey" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'Child abuse is an issue that everyone should feel passionate about stopping': Abbey and Melinda Messenger are ambassadors for NSPCC
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/femail/article-2622511/I-never-thought-Id-children-I-never-thought-Id-love-Angelina-Jolie-opens-rare-interview-Brad-babies-rebellious-twenties.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622511-1DA59B7500000578-469_154x115.jpg" height="115" width="154" alt="Jolie in Elle" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'I never thought I'd have children, I never thought I'd be in love': Angelina Jolie opens up in rare interview about Brad, babies, and her rebellious twenties
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622944/Brandi-Glanville-displays-long-legs-thigh-skimming-frock-Mothers-Day-breast-cancer-luncheon.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622944-1DA888E500000578-566_154x115.jpg" height="115" width="154" alt="She doesn't look homeless! Brandi Glanville displays her long legs at breast cancer luncheon... as she moves into new home after she was 'kicked out by landlord'" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Brandi Glanville displays her long legs in thigh-skimming frock at Mother's Day breast cancer luncheon
            </strong>
            At the Beverly Hills Four Seasons Hotel
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622526/Rooftop-hideaway-Bette-Midler-reveals-inside-stunning-multimillion-dollar-New-York-Penthouse.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622526-1DA5B5B200000578-309_154x115.jpg" height="115" width="154" alt="Rooftop hideaway! Bette Midler reveals inside her stunning multimillion dollar New York Penthouse" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Inside Bette Midler's multimillion dollar New York Penthouse
            </strong>
            Who needs the wind beneath your wings when you've Manhattan under your feet?
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622617/Justin-Timberlake-looks-casual-leaves-Copenhagen-hotel-wavy-haired-mom-Lynn-ahead-gig.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622617-1DA60A0500000578-970_154x115.jpg" height="115" width="154" alt="That's where you get your curls from! Justin Timberlake looks casual as he leaves Copenhagen hotel with his wavy-haired mom Lynn ahead of gig" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            That's where you get your curls from! Justin Timberlake looks casual as he leaves Copenhagen hotel with his wavy-haired mom Lynn ahead of gig
            </strong>
            
          </span>
        </a>
      </li>
      <li>
        <a href="/tvshowbiz/article-2622953/Tim-Robards-jokes-trying-Californian-holiday-Anna-Heinrich-quiet-share-entire-trip-social-media.html" class="bottom">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622953-1DA8C31900000578-745_154x115.jpg" height="115" width="154" alt="'You couldn't tell we were tourists at all:' Tim Robards jokes about trying to keep Californian holiday with Anna Heinrich quiet...while they share the entire trip on social media" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            'For us, it's all about being together': The Bachelor Australia's Tim Robards and Anna Heinrich reveal they are still madly in love seven months on from show
            </strong>
            
          </span>
        </a>
      </li>
    </ul>
    
  </div>

  </div>
  <script type="text/javascript">
    DM.has('p-1419', 'comScore', {
      mo_mod_id: '1000114',
      mo_mod_pos: 'p-1419'
    });
  </script>

        <div class="item mpu_wrapper">
    <div class="mpu adHolder molads_mpu_bottom" id="p-1420">
    <script type="text/javascript">
      adverts.addToArray({type:'300x250', pos:'mpu_bottom', adProbe:false});
    </script>
  </div>
  </div>

  </div>
  </div>
    <div class="gamma">
        <div class="home item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

        <div class="item traffic_heat_maps_wrapper">
    <div class="full-infographic">
    <!--[if gte IE 9]><!-->
  <div class='infographic first'>
    <h2 class='lb-hdr'>UK TRAFFIC HEAT MAP</h2>
    <div class='maps gr6ox'>
      <div class='info-top' id='p-1424-GB-label'>
        <span class='area-label'></span>
        <span class='area-value'></span>
      </div>
      <div class='info-bottom xogr1'>
        <p class='xogr2'>TOTAL ARTICLE VIEWS</p>
        <div>
          <span class='count-label last-hour'>LAST HOUR</span>
          <span class='count-value last-hour'>634,306</span>
          <span class='count-label today'>TODAY</span>
          <span class='count-value today'>11,697,995</span>
        </div>
      </div>
      <svg class='GB' id='p-1424-GB-map'>
      </svg>
      <div class='zoom in' id='p-1424-GB-zoom-in' title='Zoom In'>+</div>
      <div class='zoom out' id='p-1424-GB-zoom-out' title='Zoom Out'>-</div>
    </div>
  </div>
  <script type="text/javascript">
  AND.addScript(DM.guntherBase + 'leaderboards-maps.js', function () {
    GBmap('p-1424-GB', {U4:[594.0, '594'],Y8:[652.0, '652'],R7:[92.0, '92'],D6:[1879.0, '1,879'],N3:[1367.0, '1,367'],Z2:[287.0, '287'],A9:[1378.0, '1,378'],F2:[9251.0, '9,251'],W8:[68.0, '68'],S4:[60.0, '60'],N9:[891.0, '891'],J5:[1130.0, '1,130'],A7:[12066.0, '12,066'],F1:[75.0, '75'],J6:[1460.0, '1,460'],J7:[2652.0, '2,652'],W7:[483.0, '483'],N8:[2792.0, '2,792'],F3:[83.0, '83'],J4:[1131.0, '1,131'],Z1:[2353.0, '2,353'],A8:[1422.0, '1,422'],S3:[171.0, '171'],J8:[6822.0, '6,822'],S6:[351.0, '351'],J3:[770.0, '770'],F4:[1714.0, '1,714'],N7:[11753.0, '11,753'],E9:[440.0, '440'],A5:[4255.0, '4,255'],O2:[925.0, '925'],S5:[361.0, '361'],J9:[3544.0, '3,544'],F5:[420.0, '420'],J2:[1225.0, '1,225'],N6:[1447.0, '1,447'],B1:[1526.0, '1,526'],A6:[975.0, '975'],O1:[909.0, '909'],W9:[1234.0, '1,234'],28:[67.0, '67'],S9:[117.0, '117'],A2:[785.0, '785'],O5:[23.0, '23'],E6:[5288.0, '5,288'],K1:[1358.0, '1,358'],X4:[897.0, '897'],Y4:[1021.0, '1,021'],I9:[6866.0, '6,866'],E5:[897.0, '897'],A1:[1325.0, '1,325'],Y3:[242.0, '242'],O6:[395.0, '395'],K2:[6492.0, '6,492'],X5:[3547.0, '3,547'],T1:[297.0, '297'],S7:[79.0, '79'],E8:[11.0, '11'],Y2:[318.0, '318'],A4:[1228.0, '1,228'],O3:[870.0, '870'],X6:[302.0, '302'],T2:[357.0, '357'],T3:[60.0, '60'],X7:[706.0, '706'],S8:[36.0, '36'],A3:[892.0, '892'],Y1:[522.0, '522'],O4:[381.0, '381'],E7:[35.0, '35'],E1:[951.0, '951'],X9:[597.0, '597'],M9:[1748.0, '1,748'],T5:[2342.0, '2,342'],M8:[65.0, '65'],I4:[688.0, '688'],B8:[2348.0, '2,348'],P1:[83.0, '83'],X8:[463.0, '463'],M7:[842.0, '842'],I3:[2097.0, '2,097'],E2:[3148.0, '3,148'],B9:[3525.0, '3,525'],T4:[12.0, '12'],I6:[3333.0, '3,333'],I7:[4254.0, '4,254'],I2:[12363.0, '12,363'],T7:[641.0, '641'],E3:[796.0, '796'],M6:[73.0, '73'],B6:[3387.0, '3,387'],P3:[3952.0, '3,952'],T6:[752.0, '752'],I8:[43.0, '43'],E4:[11177.0, '11,177'],M5:[1372.0, '1,372'],Q9:[236.0, '236'],I1:[2237.0, '2,237'],B7:[6667.0, '6,667'],P2:[1716.0, '1,716'],B3:[966.0, '966'],P6:[5670.0, '5,670'],F7:[1100.0, '1,100'],L2:[1183.0, '1,183'],W3:[14.0, '14'],X3:[639.0, '639'],F6:[2560.0, '2,560'],B2:[1823.0, '1,823'],P7:[1492.0, '1,492'],X2:[402.0, '402'],L3:[1287.0, '1,287'],W4:[642.0, '642'],T8:[331.0, '331'],F9:[1043.0, '1,043'],X1:[181.0, '181'],B5:[383.0, '383'],P4:[1199.0, '1,199'],W5:[1434.0, '1,434'],S1:[172.0, '172'],W6:[331.0, '331'],T9:[600.0, '600'],L1:[1605.0, '1,605'],B4:[3194.0, '3,194'],P5:[83.0, '83'],F8:[9929.0, '9,929'],S2:[113.0, '113'],H3:[9658.0, '9,658'],L8:[690.0, '690'],Q2:[528.0, '528'],L7:[981.0, '981'],C9:[2411.0, '2,411'],U6:[455.0, '455'],H4:[5746.0, '5,746'],H2:[7825.0, '7,825'],U5:[31.0, '31'],D1:[723.0, '723'],Y9:[1067.0, '1,067'],H5:[2365.0, '2,365'],L6:[1488.0, '1,488'],L9:[6600.0, '6,600'],Q1:[2054.0, '2,054'],H1:[42.0, '42'],Q4:[3800.0, '3,800'],D2:[2395.0, '2,395'],L5:[401.0, '401'],U8:[5410.0, '5,410'],H6:[55.0, '55'],P9:[1564.0, '1,564'],C7:[2738.0, '2,738'],U7:[40.0, '40'],Q3:[2729.0, '2,729'],H7:[5161.0, '5,161'],L4:[335.0, '335'],P8:[3167.0, '3,167'],D3:[3695.0, '3,695'],C8:[3343.0, '3,343'],Q7:[310.0, '310'],M3:[3843.0, '3,843'],C4:[14.0, '14'],Z6:[67.0, '67'],G8:[2745.0, '2,745'],W2:[1123.0, '1,123'],V2:[8332.0, '8,332'],G7:[1875.0, '1,875'],C3:[4809.0, '4,809'],Q8:[63.0, '63'],W1:[825.0, '825'],M4:[4892.0, '4,892'],Z7:[101.0, '101'],V3:[490.0, '490'],Z8:[31.0, '31'],Q5:[2043.0, '2,043'],U9:[1259.0, '1,259'],M1:[2082.0, '2,082'],C6:[2658.0, '2,658'],V4:[402.0, '402'],V5:[542.0, '542'],Q6:[205.0, '205'],C5:[5192.0, '5,192'],G9:[267.0, '267'],M2:[1118.0, '1,118'],R1:[67.0, '67'],G2:[938.0, '938'],R3:[2864.0, '2,864'],K6:[2062.0, '2,062'],V7:[537.0, '537'],G3:[27.0, '27'],K7:[3751.0, '3,751'],R2:[75.0, '75'],G1:[1844.0, '1,844'],V6:[340.0, '340'],O9:[120.0, '120'],K5:[1010.0, '1,010'],G4:[72.0, '72'],K8:[1475.0, '1,475'],K9:[1844.0, '1,844'],C1:[405.0, '405'],K4:[2342.0, '2,342'],V9:[15.0, '15'],G5:[9048.0, '9,048'],O8:[2065.0, '2,065'],D8:[2774.0, '2,774'],N1:[3499.0, '3,499'],R4:[181.0, '181'],K3:[2030.0, '2,030'],G6:[2426.0, '2,426'],C2:[1712.0, '1,712'],O7:[3852.0, '3,852'],D9:[822.0, '822'],V8:[1334.0, '1,334'],R8:[273.0, '273'],N4:[3295.0, '3,295'],Z5:[175.0, '175'],D5:[1932.0, '1,932'],H9:[78970.0, '78,970'],U1:[354.0, '354'],V1:[2462.0, '2,462'],Y5:[684.0, '684'],H8:[7204.0, '7,204'],D4:[3736.0, '3,736'],R9:[133.0, '133'],N5:[3602.0, '3,602'],J1:[4899.0, '4,899'],Y6:[1293.0, '1,293'],U2:[848.0, '848'],Z4:[1093.0, '1,093'],R6:[268.0, '268'],N2:[2030.0, '2,030'],D7:[2153.0, '2,153'],Y7:[192.0, '192'],U3:[1008.0, '1,008'],Z3:[681.0, '681']});
  });
  </script>
  <![endif]-->

    <!--[if gte IE 9]><!-->
  <div class='infographic '>
    <h2 class='lb-hdr'>GLOBAL TRAFFIC HEAT MAP</h2>
    <div class='maps gr6ox'>
      <div class='info-top' id='p-1424-World-label'>
        <span class='area-label'></span>
        <span class='area-value'></span>
      </div>
      <div class='info-bottom xogr1'>
        <p class='xogr2'>TOTAL ARTICLE VIEWS</p>
        <div>
          <span class='count-label last-hour'>LAST HOUR</span>
          <span class='count-value last-hour'>1,236,514</span>
          <span class='count-label today'>TODAY</span>
          <span class='count-value today'>25,224,156</span>
        </div>
      </div>
      <svg class='World' id='p-1424-World-map'>
      </svg>
      <div class='zoom in' id='p-1424-World-zoom-in' title='Zoom In'>+</div>
      <div class='zoom out' id='p-1424-World-zoom-out' title='Zoom Out'>-</div>
    </div>
  </div>
  <script type="text/javascript">
  AND.addScript(DM.guntherBase + 'leaderboards-maps.js', function () {
    Worldmap('p-1424-World', {LK:[650.0, '650'],UZ:[53.0, '53'],ME:[131.0, '131'],CU:[5.0, '5'],IN:[14146.0, '14,146'],GY:[81.0, '81'],MR:[2.0, '2'],AF:[129.0, '129'],MY:[3038.0, '3,038'],AL:[704.0, '704'],RS:[1353.0, '1,353'],AM:[147.0, '147'],MX:[1915.0, '1,915'],IT:[4046.0, '4,046'],MC:[147.0, '147'],VA:[3.0, '3'],NO:[3712.0, '3,712'],DZ:[350.0, '350'],MZ:[83.0, '83'],MW:[143.0, '143'],BB:[517.0, '517'],IS:[603.0, '603'],MD:[159.0, '159'],VC:[67.0, '67'],RU:[1665.0, '1,665'],AO:[72.0, '72'],IR:[162.0, '162'],ES:[7384.0, '7,384'],MV:[570.0, '570'],FI:[5431.0, '5,431'],MA:[548.0, '548'],BE:[5090.0, '5,090'],JM:[1001.0, '1,001'],VE:[372.0, '372'],ET:[400.0, '400'],IQ:[323.0, '323'],MU:[1314.0, '1,314'],AP:[97.0, '97'],BD:[758.0, '758'],NP:[242.0, '242'],AI:[11.0, '11'],KG:[8.0, '8'],PK:[3911.0, '3,911'],A2:[18.0, '18'],JP:[569.0, '569'],SO:[53.0, '53'],BH:[335.0, '335'],TO:[5.0, '5'],A1:[294.0, '294'],GD:[105.0, '105'],TN:[233.0, '233'],BI:[9.0, '9'],KH:[57.0, '57'],QA:[1179.0, '1,179'],OM:[285.0, '285'],CA:[32702.0, '32,702'],GE:[219.0, '219'],FJ:[53.0, '53'],BF:[6.0, '6'],TM:[7.0, '7'],SR:[110.0, '110'],UG:[874.0, '874'],GF:[9.0, '9'],RW:[221.0, '221'],PH:[1254.0, '1,254'],JO:[278.0, '278'],BG:[1218.0, '1,218'],HT:[89.0, '89'],CD:[26.0, '26'],YE:[146.0, '146'],GH:[1383.0, '1,383'],AW:[36.0, '36'],UA:[545.0, '545'],DO:[896.0, '896'],LY:[78.0, '78'],GG:[613.0, '613'],LV:[552.0, '552'],HR:[1312.0, '1,312'],AX:[1.0, '1'],HU:[2065.0, '2,065'],DM:[28.0, '28'],SV:[135.0, '135'],LU:[477.0, '477'],PY:[49.0, '49'],CF:[1.0, '1'],AU:[6260.0, '6,260'],KN:[21.0, '21'],LT:[1387.0, '1,387'],GI:[364.0, '364'],NC:[20.0, '20'],GB:[634306.0, '634,306'],SY:[86.0, '86'],AR:[1051.0, '1,051'],CI:[79.0, '79'],SN:[102.0, '102'],GM:[69.0, '69'],VG:[85.0, '85'],GA:[15.0, '15'],EU:[1127.0, '1,127'],KE:[2519.0, '2,519'],SZ:[24.0, '24'],KR:[257.0, '257'],ZW:[329.0, '329'],GN:[6.0, '6'],RO:[2546.0, '2,546'],ZM:[335.0, '335'],RE:[23.0, '23'],VI:[47.0, '47'],CG:[3.0, '3'],AT:[3337.0, '3,337'],SL:[148.0, '148'],NA:[311.0, '311'],NL:[15847.0, '15,847'],VU:[3.0, '3'],BA:[528.0, '528'],SK:[930.0, '930'],CH:[5114.0, '5,114'],BZ:[67.0, '67'],GL:[8.0, '8'],GR:[2437.0, '2,437'],KW:[540.0, '540'],CO:[611.0, '611'],CN:[557.0, '557'],SI:[966.0, '966'],DE:[12662.0, '12,662'],GQ:[4.0, '4'],TT:[924.0, '924'],GT:[107.0, '107'],BY:[74.0, '74'],CM:[54.0, '54'],CL:[472.0, '472'],GP:[13.0, '13'],KY:[286.0, '286'],PS:[76.0, '76'],SG:[1987.0, '1,987'],TW:[237.0, '237'],GU:[13.0, '13'],HK:[973.0, '973'],TC:[37.0, '37'],KZ:[135.0, '135'],PR:[459.0, '459'],SH:[2.0, '2'],CR:[231.0, '231'],BW:[232.0, '232'],CK:[9.0, '9'],SD:[100.0, '100'],TZ:[692.0, '692'],NI:[24.0, '24'],JE:[892.0, '892'],LR:[79.0, '79'],BS:[265.0, '265'],HN:[71.0, '71'],DJ:[38.0, '38'],IE:[26654.0, '26,654'],BR:[2351.0, '2,351'],LS:[15.0, '15'],DK:[4467.0, '4,467'],SC:[47.0, '47'],PT:[2367.0, '2,367'],NG:[6136.0, '6,136'],EC:[131.0, '131'],US:[282521.0, '282,521'],MK:[349.0, '349'],AZ:[165.0, '165'],ML:[6.0, '6'],SE:[4855.0, '4,855'],BT:[15.0, '15'],VN:[333.0, '333'],BN:[112.0, '112'],BM:[304.0, '304'],NZ:[5285.0, '5,285'],TJ:[2.0, '2'],PF:[47.0, '47'],LB:[560.0, '560'],CY:[1649.0, '1,649'],MN:[10.0, '10'],FR:[15294.0, '15,294'],BO:[77.0, '77'],EE:[1338.0, '1,338'],PG:[7.0, '7'],LC:[180.0, '180'],MM:[46.0, '46'],CZ:[1403.0, '1,403'],FO:[62.0, '62'],TH:[943.0, '943'],AD:[29.0, '29'],CW:[205.0, '205'],SA:[1585.0, '1,585'],IL:[2033.0, '2,033'],LA:[23.0, '23'],PE:[435.0, '435'],EG:[1566.0, '1,566'],MO:[13.0, '13'],BJ:[30.0, '30'],SB:[5.0, '5'],PL:[3287.0, '3,287'],MH:[2.0, '2'],ID:[1478.0, '1,478'],MS:[17.0, '17'],AG:[125.0, '125'],PA:[122.0, '122'],PM:[1.0, '1'],MG:[23.0, '23'],MT:[2448.0, '2,448'],ZA:[9868.0, '9,868'],LI:[4.0, '4'],TG:[39.0, '39'],UY:[135.0, '135'],IM:[874.0, '874'],MQ:[8.0, '8'],AE:[5800.0, '5,800'],CV:[12.0, '12'],TR:[2709.0, '2,709']});
  });
  </script>
  <![endif]-->

    <!--[if gte IE 9]><!-->
  <div class='infographic '>
    <h2 class='lb-hdr'>US TRAFFIC HEAT MAP</h2>
    <div class='maps gr6ox'>
      <div class='info-top' id='p-1424-US-label'>
        <span class='area-label'></span>
        <span class='area-value'></span>
      </div>
      <div class='info-bottom xogr1'>
        <p class='xogr2'>TOTAL ARTICLE VIEWS</p>
        <div>
          <span class='count-label last-hour'>LAST HOUR</span>
          <span class='count-value last-hour'>282,521</span>
          <span class='count-label today'>TODAY</span>
          <span class='count-value today'>5,053,572</span>
        </div>
      </div>
      <svg class='US' id='p-1424-US-map'>
      </svg>
      <div class='zoom in' id='p-1424-US-zoom-in' title='Zoom In'>+</div>
      <div class='zoom out' id='p-1424-US-zoom-out' title='Zoom Out'>-</div>
    </div>
  </div>
  <script type="text/javascript">
  AND.addScript(DM.guntherBase + 'leaderboards-maps.js', function () {
    USmap('p-1424-US', {ME:[802.0, '802'],DC:[3292.0, '3,292'],IN:[2889.0, '2,889'],IA:[1545.0, '1,545'],AL:[3622.0, '3,622'],VA:[8194.0, '8,194'],AK:[465.0, '465'],MD:[5582.0, '5,582'],MA:[6736.0, '6,736'],AP:[5.0, '5'],OK:[2315.0, '2,315'],FL:[13690.0, '13,690'],TN:[3665.0, '3,665'],CA:[32500.0, '32,500'],WV:[582.0, '582'],ND:[434.0, '434'],RI:[946.0, '946'],NE:[1268.0, '1,268'],OR:[3145.0, '3,145'],NC:[6187.0, '6,187'],WY:[279.0, '279'],NJ:[10177.0, '10,177'],AR:[1148.0, '1,148'],GA:[6812.0, '6,812'],OH:[6601.0, '6,601'],VT:[433.0, '433'],NM:[1166.0, '1,166'],CO:[4551.0, '4,551'],DE:[981.0, '981'],HI:[973.0, '973'],KY:[1802.0, '1,802'],KS:[1713.0, '1,713'],MI:[4568.0, '4,568'],SD:[473.0, '473'],NH:[830.0, '830'],SC:[2724.0, '2,724'],TX:[19418.0, '19,418'],AZ:[4554.0, '4,554'],UT:[1549.0, '1,549'],WI:[3155.0, '3,155'],NY:[24690.0, '24,690'],MN:[4103.0, '4,103'],WA:[6580.0, '6,580'],IL:[8658.0, '8,658'],NV:[1873.0, '1,873'],LA:[2144.0, '2,144'],MO:[4199.0, '4,199'],ID:[714.0, '714'],MS:[1042.0, '1,042'],CT:[3400.0, '3,400'],PA:[8763.0, '8,763'],MT:[504.0, '504'],AE:[142.0, '142']});
  });
  </script>
  <![endif]-->

  </div>


  </div>

  </div>
    <div class="gamma">
        <div class="item video_carousel_module_wrapper">
    <div class="tvshowbiz  video_carousel_container cleared" id="p-1428"
       data-track-module="sm-723^video_carousel_module"
       data-track-selector=".videoLink"
       data-track-type="cl">
      <div class="video_carousel_title bdrcc">
        <div class="wocc carousel-title">VIDEO</div>
        <img src="http://i.dailymail.co.uk/i/furniture/standard_modules/video/icon_filmstrip.png" />
        <div class="channel-title">WATCH: TODAY'S TOP SHOWBIZ VIDEOS</div>
        <div class="rotator-title">
          <ul class="rotator-pages">
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="1"><span class="usability">1</span></a>
            </li>
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="2"><span class="usability">2</span></a>
            </li>
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="3"><span class="usability">3</span></a>
            </li>
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="4"><span class="usability">4</span></a>
            </li>
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="5"><span class="usability">5</span></a>
            </li>
          </ul>
        </div>
      </div>

      <div class="video-carousel-body">
        <div class="link-wox linkro-ccox left">
          <a class="js-move-prev" href="#">
            <div class="left_scroll"><span></span></div>
          </a>
          <div class="blank-div"></div>
        </div>
        <div class="rotator link-wocc linkro-womlcc">
          <ul class="js-itemList rotator-panels">
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1093968/Kerry-Katona-shows-baby-number-traumatic-birth.html"
                data-videoid="3543795860001"
                data-channel="tvshowbiz"
                data-source="ITV"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093968&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA5557000000578-43_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>29327</p></div>
                <div class="video-item-title bdrcc">Kerry Katona shows off baby number five after traumatic birth and she says she may not be...</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1093961/Best-friend-Jane-Katies-marries-Kieran.html"
                data-videoid="3543616251001"
                data-channel="tvshowbiz"
                data-source="Splash"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093961&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA5141A00000578-379_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>100496</p></div>
                <div class="video-item-title bdrcc">Best friend Jane Pountney by Katie's side as she marries Kieran Hayler</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1094006/Jordanian-TV-guests-destroy-7-stars-news-studio-live-show.html"
                data-videoid="3545886210001"
                data-channel="tvshowbiz"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094006&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA9704C00000578-324_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>26494</p></div>
                <div class="video-item-title bdrcc">Jordanian TV guests destroy the 7 stars news studio during live show</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1094122/Exciting-trailer-Dawn-Of-The-Planet-Of-The-Apes.html"
                data-videoid="3546762583001"
                data-channel="tvshowbiz"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094122&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DACDCF200000578-148_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>148097</p></div>
                <div class="video-item-title bdrcc">Get ready for the sequel! Dawn Of The Planet Of The Apes takes the story to the next level</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1094042/West-Kardashian-wedding-style-Vogue.html"
                data-videoid="3373725835001"
                data-channel="tvshowbiz"
                data-source="Reuters"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094042&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/03/21/video-undefined-1C7A58EE00000578-566_636x358.jpg" alt=""/>
                <div class="video-item-time"><p></p></div>
                <div class="video-item-title bdrcc">Kanye West and Kim Kardashian show off their wedding style in Vogue</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1094135/Seth-Rogen-jokes-Justin-Beiber-douchbag.html"
                data-videoid="3546593105001"
                data-channel="tvshowbiz"
                data-source="PR"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094135&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DABA4D200000578-583_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>119723</p></div>
                <div class="video-item-title bdrcc">Seth Rogen jokes on the Daily Show about Justin Beiber being a douchbag</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1094072/Naomi-Watts-looks-gorgeous-Met-Gala-New-York.html"
                data-videoid="3540569755001"
                data-channel="tvshowbiz"
                data-source="Reuters"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094072&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA9B4D400000578-873_636x358.jpg" alt=""/>
                <div class="video-item-time"><p></p></div>
                <div class="video-item-title bdrcc">Naomi Watts looks gorgeous at fashion's most extravagant evening</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1093997/Lindsay-Lohan-takes-plunge-London-fundraiser.html"
                data-videoid="3545201030001"
                data-channel="tvshowbiz"
                data-source="Other"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093997&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA85AB500000578-209_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>32323</p></div>
                <div class="video-item-title bdrcc">Lindsay Lohan takes the plunge in peacock dress at London fundraiser</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1094010/From-archive-Chantelle-smiles-adorable-Dolly.html"
                data-videoid="3399892630001"
                data-channel="tvshowbiz"
                data-source="Other"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094010&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/03/27/video-undefined-1C9FDC0F00000578-764_636x358.jpg" alt=""/>
                <div class="video-item-time"><p></p></div>
                <div class="video-item-title bdrcc">From the archive: Chantelle Houghton at lunch with BF and adorable daughter Dolly</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1094008/Jen-Lawrence-Liam-Hemsworth-Hunger-Games-set-Paris.html"
                data-videoid="3545959091001"
                data-channel="tvshowbiz"
                data-source="StormShadow"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094008&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA985A100000578-362_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>103770</p></div>
                <div class="video-item-title bdrcc">Jennifer Lawrence and Liam Hemsworth shooting scenes for The Hunger Games in Paris</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1094038/Swashbuckling-Jackman-practises-ahead-new-film.html"
                data-videoid="3545501676001"
                data-channel="tvshowbiz"
                data-source="Other"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094038&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA8EC2F00000578-658_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>93995</p></div>
                <div class="video-item-title bdrcc">Swashbuckling Hugh Jackman in practise ahead of new film</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1087611/Nun-stuns-crowd-judges-Italys-The-Voice.html"
                data-videoid="3372072469001"
                data-channel="tvshowbiz"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1087611&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/03/21/video-undefined-1C78787200000578-631_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>104680</p></div>
                <div class="video-item-title bdrcc">Nun stuns the crowd and the judges during blind auditions on Italy's The Voice</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1093959/Kim-Kardashian-unwittingly-gets-selfied-fans-photo.html"
                data-videoid="3543609044001"
                data-channel="tvshowbiz"
                data-source="Splash"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093959&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA4B6D700000578-375_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>39614</p></div>
                <div class="video-item-title bdrcc">Kim Kardashian unwittingly gets selfied in fan's photo after he sneaks up and snaps her</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1094094/Victoria-Hervey-celebs-attending-Gabrielles-Gala-event.html"
                data-videoid="3546167464001"
                data-channel="tvshowbiz"
                data-source="XPOSURE"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094094&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DAA88B800000578-860_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>29954</p></div>
                <div class="video-item-title bdrcc">Victoria Hervey steps out in a very revealing ensemble as she attended Gabrielle's Gala...</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1093957/Archive-Katie-Kieran-February-shock-split-news.html"
                data-videoid="3543551029001"
                data-channel="tvshowbiz"
                data-source="Splash"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093957&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA4484F00000578-782_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>105680</p></div>
                <div class="video-item-title bdrcc">Archive: Katie and Kieran at the Robocop premiere in February before shock split news</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/tvshowbiz/video-1093040/Ellen-Page-discusses-moment-revealed-shes-gay.html"
                data-videoid="3525701208001"
                data-channel="tvshowbiz"
                data-source="PR"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093040&amp;colour=tvshowbiz&amp;item-type=sm&amp;item-id=723 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D7C779300000578-508_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>99777</p></div>
                <div class="video-item-title bdrcc">Ellen Page discusses the moment she publicly revealed she's gay</div>
              </a>
            </li>
          </ul>
        </div>
        <div class="link-wox linkro-ccox right">
          <a class="js-move-next" href="#">
            <div class="right_scroll"><span></span></div>
          </a>
          <div class="blank-div"></div>
        </div>
      </div>
  </div>
  <script type="text/javascript">
  DM.has("p-1428", 'videoChannelCarouselModule',
         {"player" : "1989148206001",
          "playerKey" : "AQ~~,AAAAAFSL1bg~,CmS1EFtcMWELN_eSE9A7gpcGWF5XAVmI",
          "nonEmbeddablePlayerIdent" : "2572801325001",
          "nonEmbeddablePlayerKey" : "AQ~~,AAAAAFSL1bg~,CmS1EFtcMWF3nDd2YNUcSIWL0H_o4As-",
          "trackingType" : "carousel_triple",
          "channelShortName" : "tvshowbiz",
          "overlayType" : "carousel",
          "pageCount" : "5",
          "pageSize" : 3,
          "onPos": 0,
          "updateStyleOnHover": true,
          "videoPlayerConfigMap": {'3543795860001' : 'false','3543616251001' : 'false','3545886210001' : 'false','3546762583001' : 'false','3373725835001' : 'false','3546593105001' : 'false','3540569755001' : 'false','3545201030001' : 'false','3399892630001' : 'false','3545959091001' : 'false','3545501676001' : 'false','3372072469001' : 'false','3543609044001' : 'false','3546167464001' : 'false','3543551029001' : 'false','3525701208001' : 'false'},
          "rsi" : typeof(adverts) != 'undefined' && typeof (adverts.getRsiValues) != 'undefined' ? adverts.getRsiValues() : null
  });
  </script>


  </div>

        <div class="home item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

  </div>
    <div class="cleared">
        <div class="alpha">
     <div class="femail item">
    <div class="puffeditor wob cleared" id="p-1434">
        <img  src="http://i.dailymail.co.uk/i/pix/2013/01_04/sleeves_306x325.jpg" height="325" width="306" alt="janet ellis" />
    <div class="pufftext">
      <h3>IN FEMAIL TODAY...</h3>
      <ul class="ccob link-wox linkro-lccox">
        <li>HATE YOUR BINGO WINGS?:
          <a href="/femail/article-2622684/Hate-bingo-wings-Take-peek-peekaboo-sleeves-says-JANET-ELLIS.html">Janet Ellis tried six dresses with flattering sleeves</a>
        </li>
        <li>A LIVING BEREAVEMENT:
          <a href="/femail/article-2622802/A-living-bereavement-When-ESTHER-RANTZEN-spoke-couples-denied-access-grandchildren-triggered-flood-heart-rending-stories-revealing-agony-family-breakdowns-forgotten-victims.html">Couples denied access to their grandchildren</a>
        </li>
        <li>TRY TELLING MY LITTLE GIRL IT'S SEXIST TO LOVE PINK!:
          <a href="/femail/article-2622736/Try-telling-little-girl-sexist-love-pink-ANGELA-EPSTEIN-says-warnings-against-letting-girls-love-pink-Lefty-hokum.html">Angela Epstein denounces 'Lefty hokum'</a>
        </li>
        <li>CURLY GIRLS OF THE WORLD UNITE:
          <a href="/femail/article-2622872/Curly-girls-world-unite-lets-end-tyranny-straighteners-says-JILL-FOSTER.html">Lets end the tyranny of straighteners</a>
        </li>
        <li>THINK CANNABIS IS HARMLESS? READ ON:
          <a href="/femail/article-2622755/The-mothers-story-says-cannabis-harmless-MUST-read-Henry-came-wealthy-family-golden-future-life-tatters-thanks-drug.html">Mother's tragic tale of her son's death</a>
        </li>
        <li>HOW DOES 'BOTOX FREE' FELICITY KENDAL LOOK THIS GOOD?:
          <a href="/femail/article-2622891/How-does-Botox-free-Felicity-Kendal-look-good-67.html">Still sexy at 67</a>
        </li>
      </ul>
    </div>
  </div>
  </div>
  <script type="text/javascript">
    DM.has('p-1434', 'comScore', {
      mo_mod_id: '1000030',
      mo_mod_pos: 'p-1434'
    });
  </script>

     <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

     <div class="home item html_snippet_module">
    <div id='taboola-mid-page'></div>
    <script type="text/javascript">
    window._taboola = window._taboola || [];
    _taboola.push({mode:'thumbs-1r', container:'taboola-mid-page', placement:'uk-homepage'});
  </script>
  </div>

     <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

     <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline120}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623222/An-English-manor-heart-Washington-How-British-Embassy-hosted-Churchill-Liz-Taylor-helped-build-special-relationship.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623222-1DAAFAE800000578-548_636x382.jpg" height="382" width="636" alt="A butler carries an urn of tea to prepare for Britain's Prince Harry" />
        </a>
      <div >
       <p>
         
         The 1920s ambassador's residence (left and inset) is the only U.S. building by the renowned architect Sir Edward Lutyens, who designed it like a Georgian manor with a sweeping ballroom and eight acres of gardens. Its guests have ranged from George VI and Winston Churchill (bottom right with General George C Marshall) to the Beatles and the actress Elizabeth Taylor (top right with her husband Jack Warner meeting Elizabeth II and Gerald Ford). Now a new book by historian Dr Anthony Seldon explores its history. He writes how the building is a visual symbol of the 'special relationship' between the U.S. and Britain - but reveals diplomats still made several complaints, including that the doorway was too small and dark.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623222/An-English-manor-heart-Washington-How-British-Embassy-hosted-Churchill-Liz-Taylor-helped-build-special-relationship.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623222">          25</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Ru1HFC| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623222-1DAAFAE800000578-141_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline121}}</a>
    </h2>
    <div class="articletext">
      <a href="/sciencetech/article-2622458/Google-Maps-gets-upgrade-Update-tells-lane-drive-lets-download-maps-use-offline.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622458-1DA51E5E00000578-995_154x115.jpg" height="84" width="112" alt="Google has rolled out an update on Android and iOS for its Maps app. Amongst other new features, now when navigating a route the app will tell you what lane to be in, ensuring you don't miss your exit or turning" />
      </a>
      <p>
        
        Google has released a new update for its Maps app on iOS and Android. Amongst a number of new features is the ability to save maps offline.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/sciencetech/article-2622458/Google-Maps-gets-upgrade-Update-tells-lane-drive-lets-download-maps-use-offline.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622458">          97</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RrpAxA| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622458-1DA51E5E00000578-235_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline122}}</a>
    </h2>
    <div class="articletext">
      <a href="/travel/article-2623168/Football-mad-boyfriend-cuts-short-romantic-luxury-holiday-Mexico-fly-home-play-local-PUB-TEAM.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623168-1DA2365300000578-151_154x115.jpg" height="84" width="112" alt="Dream holiday: Chris Jones, who plays for Max United, cut his Mexico trip short to play for his team" />
      </a>
      <p>
        
        Chris Jones, 26, from Cardiff, borrowed £1,100 from his mum to get on a plane to make the 5,000-mile trip home halfway through the dream trip with his girlfriend.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="travelmail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/travel/article-2623168/Football-mad-boyfriend-cuts-short-romantic-luxury-holiday-Mexico-fly-home-play-local-PUB-TEAM.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623168">          29</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEWEAB| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623168-1DA2365300000578-200_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline123}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2622477/Queen-Duke-Edinburgh-salute-work-Journalists-Charity-London-reception-mark-150-years-founded-Dickens.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622477-1DA4F7DD00000578-743_154x115.jpg" height="84" width="112" alt="The Queen helped celebrate the 150th anniversary of the Journalists' Charity at a reception in London today - accompanied by its chairman, Laurie Upshon, she met editors and broadcasters at the Stationers' Hall" />
      </a>
      <p>
        
        The 88-year-old monarch, who is patron of the charity which helps reporters and their families, attended its anniversary celebrations at the Stationers' Hall in central London today.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first gr3ox">
    <a class="http://dailym.ai/RrxJ56| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622477-1DA4B7AD00000578-770_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline124}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2622549/Blind-lemur-British-vets-saved-sight-pioneering-two-hour-operation-remove-cataracts.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-0-1DA4FB3F00000578-931_154x115.jpg" height="84" width="112" alt="A blind lemur can now see again thanks to a pioneering operation by British vets" />
      </a>
      <p>
        
        The four-year-old animal named Sam lost his sight at Durrell Wildlife Park, Jersey - and was saved by two British vets who flew over from the mainland.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2622549/Blind-lemur-British-vets-saved-sight-pioneering-two-hour-operation-remove-cataracts.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622549">          32</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2622549/Blind-lemur-British-vets-saved-sight-pioneering-two-hour-operation-remove-cataracts.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RrAkfA| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622549-1DA595E300000578-938_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>
    <div class="money item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline125}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623277/The-day-young-Princess-Elizabeth-celebrated-jubilant-nation-Trafalgar-Square-awash-flags-recreation-VE-day-exactly-69-years-real-thing.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623277-1DAB96B600000578-471_636x382.jpg" height="382" width="636" alt="day" />
        </a>
      <div >
       <p>
         
         Victory in Europe Day, generally known as VE Day, was celebrated on May 8 1945 to mark the unconditional surrender of Nazi Germany. Scores of party-goers flocked to the capital to honour the official end of the Second World War in Europe. Now, as these pictures show, a new film - called Girl's Night Out - is being filmed on location which imagines that among the dancing crowd were two young princesses - Elizabeth (inset) and Margaret.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623277/The-day-young-Princess-Elizabeth-celebrated-jubilant-nation-Trafalgar-Square-awash-flags-recreation-VE-day-exactly-69-years-real-thing.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623277">          37</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Rugpwm| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623277-1DAB283F00000578-185_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


  </div>

        <div class="beta">
        <div class="news item">
    <div class="js-picture-swap picture-swap ccogr2 cleared" id="p-1505">
    <h3>WORLD NEWS</h3>
    <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623332-1DAA61E500000578-36_308x185.jpg" alt="Change of heart: Putin, pictured during a wreath laying ceremony at the Kremlin, said that a referendum in eastern Ukraine should be postponed" width="292" height="168" id="p-1505-img" />
    <ul class="link-ccow linkro-wocc">
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623332-1DAA61E500000578-36_308x185.jpg| bold" href="/news/article-2623332/Pro-Russian-separatists-defy-Putins-plea-call-referendum-seceding-Ukraine-vow-ahead-anyway.html">Pro-Russian separatists 'defy' Putin's plea to call off referendum on seceding from Ukraine and vow to go ahead anyway</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623092-1DAB670F00000578-530_308x185.jpg|" href="/news/article-2623092/Social-worker-assessed-Pistorius-hours-shot-Reeva-tells-trial-heartbroken.html">Social worker who assessed Pistorius hours after he shot Reeva tells trial he was 'heartbroken'... as lawyer reveals athlete has SOLD the home where he gunned her down</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623422-1DACD09700000578-139_308x185.jpg| bold" href="/news/article-2623422/Hiding-butchers-Tanzania-Young-girl-seeks-refuge-witch-doctors-want-body-parts-shes-ALBINO.html">Hiding from the butchers of Tanzania: African girl among hundreds seeking refuge from murderous witch doctors who target their body parts because they're albino</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/05/article-2620615-1D96060100000578-729_308x185.jpg|" href="/news/article-2623239/Former-Boko-Haram-negotiator-says-group-plan-exchange-300-kidnapped-schoolgirls-comrades-imprisoned-Nigeria.html">Former Boko Haram negotiator says the group plan to exchange the 300 kidnapped schoolgirls for comrades imprisoned in Nigeria</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623107-1D70213B00000578-86_308x185.jpg| bold" href="/news/article-2623107/Head-South-Korean-ferry-company-vessel-overturned-killing-300-people-detained-suspicion-knowing-ship-overloaded.html">Head of South Korean ferry company whose vessel overturned, killing 300 people, is detained on suspicion of knowing the ship was overloaded</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623158-1DAA82F000000578-750_308x185.jpg|" href="/news/article-2623158/Police-threaten-strike-Brazil-World-Cup-latest-24-hour-walkout-pay.html">Police threaten to go on strike in Brazil during the World Cup after latest 24-hour walkout over pay</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623124-1DAA25D000000578-825_308x185.jpg| bold" href="/news/article-2623124/Saudi-court-sentences-liberal-blogger-ten-years-jail-1-000-lashes-orders-pay-133-000-fine-insulting-Islam.html">Saudi court sentences liberal blogger to ten years in jail, 1,000 lashes and orders him to pay a £133,000 fine for insulting Islam</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623006-1DA1A8B800000578-136_308x185.jpg|" href="/news/article-2623006/Elderly-head-one-Monacos-richest-families-fighting-life-hospital-mystery-mafia-style-shooting-Nice.html">Italian Mafia suspected of shooting 77-year-old head of one of Monacos wealthiest families in Nice as it tries to expand its French Riviera property portfolio</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623330-1DAB765400000578-254_308x185.jpg| bold" href="/news/article-2623330/Is-Inter-Stellar-Assistance-Force-Mysterious-UFO-filmed-blitzing-Taliban-base-Afghanistan.html">What is this mysterious aircraft filmed 'blitzing Taliban base in Afghanistan'? Footage shows 'UFO' blasting terrorists' encampment</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623209-1AA752ED00000578-215_308x185.jpg|" href="/news/article-2623209/Russia-plans-colonise-MOON-2030-according-leaked-government-document-says-robot-rovers-sent-2016.html">Russia plans to colonise the MOON by 2030 according to leaked government document that says robot rovers will be sent in 2016</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622210-1DA4305C00000578-116_308x185.jpg| bold" href="/news/article-2622210/First-South-Africans-born-apartheid-queue-vote-election-set-President-Jacob-Zuma-power-despite-string-scandals.html">First South African voters born after the end of apartheid queue for the ballot box in first general election since Nelson Mandela's death</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622679-1DA7285900000578-489_308x185.jpg|" href="/news/article-2622679/Show-strength-Streets-Moscow-filled-soldiers-tanks-missile-launchers-Russia-prepares-mark-anniversary-victory-Nazis-WW2.html">Show of strength: Streets of Moscow filled with soldiers, tanks and missile launchers as Russia prepares to mark the anniversary of victory over the Nazis in WW2</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2621576-1D95B49900000578-417_308x185.jpg| bold" href="/news/article-2621576/Vatican-848-priests-defrocked-abuse-04.html">Vatican reveals it has disciplined nearly 3,500 priests since 2004 for raping and molesting children and 848 of them have been defrocked</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622570-1DA5FF4700000578-432_308x185.jpg|" href="/news/article-2622570/Shocking-moment-Russian-strip-club-worker-picked-carried-obsessed-fan-forced-car-drove-home-dance-him.html">Shocking moment Russian strip club worker is picked up and carried by obsessed 'fan' who forced her into his car, drove her to his home and made her dance for him</a>
      </li>
      <li>
        <a class="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622111-1DA305E100000578-513_308x185.jpg| bold" href="/news/article-2622111/Pro-Russian-forces-use-children-human-shields-new-battles-rage-besieged-Ukrainian-city.html">'Soldier, do not shoot': Pro-Russian rebels force children to hold signs on frontline of Ukrainian civil war begging Kiev forces to retreat from besieged city</a>
      </li>
    </ul>
    <span class="tl">&nbsp;</span>
    <span class="tr">&nbsp;</span>
    <span class="bl">&nbsp;</span>
    <span class="br">&nbsp;</span>
  </div>
  <script type="text/javascript">
  DM.has("p-1505", "pictureSwap");
  </script>
  </div>
  <script type="text/javascript">
    DM.has('p-1505', 'comScore', {
      mo_mod_id: '1000006',
      mo_mod_pos: 'p-1505'
    });
  </script>

        <div class="home item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        LOOK WHO'S TALKING . . .
    </h6>
  </div>

  </div>

        <div class="item most_commented_articles_wrapper">
    <div class="lb-tabbed-pane tabbed-article-list article-list"
       data-track-module="lb-most-commented-articles^lb"
       data-track-selector=".lb-article a">
    <h2 class="lb-hdr">MOST COMMENTED ARTICLES</h2>
    <ul class="lb-tabs cleared">
      <li class="selected-tab first">UK</li>
      <li >US</li>
    </ul>
    <div class="lb-panes">
      <div class="selected-pane">
        <div class="xogr2">
          <select class="dropdown">
            <option value="all" selected data-url="/api/sm/most_commented_articles/all/gb">All Channels</option>
            <option value="news" data-url="/api/sm/most_commented_articles/news/gb">News</option>
            <option value="tvshowbiz" data-url="/api/sm/most_commented_articles/tvshowbiz/gb">TV &amp; Showbiz</option>
            <option value="sport" data-url="/api/sm/most_commented_articles/sport/gb">Sport</option>
            <option value="femail" data-url="/api/sm/most_commented_articles/femail/gb">Femail</option>
            <option value="health" data-url="/api/sm/most_commented_articles/health/gb">Health</option>
            <option value="money" data-url="/api/sm/most_commented_articles/money/gb">Money</option>
            <option value="sciencetech" data-url="/api/sm/most_commented_articles/sciencetech/gb">Science</option>
            <option value="travel" data-url="/api/sm/most_commented_articles/travel/gb">Travel</option>
          </select>
        </div>
        <ul class="lb-article">
          <li class="news first">
            <div class="link-bow linkro-ccogr2">
              <a href="/news/article-2622830/Millions-eating-halal-food-without-knowing-How-big-brand-shops-restaurants-sell-ritually-slaughtered-meat-dont-label-it.html">
                <img alt="Halal" src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622830-1DA8931E00000578-929_308x185.jpg">
                <strong>Millions are eating halal food without knowing it: How big brand shops and...</strong>
              </a>
            </div>
            <a class="comment-count" href="/news/article-2622830/Millions-eating-halal-food-without-knowing-How-big-brand-shops-restaurants-sell-ritually-slaughtered-meat-dont-label-it.html#comments">
              <b class="ico"></b>
        
        Comments (4,421)
            </a>
          </li>
          <li class="news">
            <div class="link-bow linkro-ccogr2">
              <a href="/news/article-2622254/Katie-Price-brands-Jane-Pountney-homewrecker-husband-Derrick-plays-affair.html">
                <img alt="JANE MARIE POUNTNEY STORY- PICTURED BIRCH GROVE HOUSE WEST CHILTINGTON, WEST SUSSEX - KATIE PRICE ARRIVES AT THE HOUSE\nKatie Price\n\\n\\n !!!!! PICTURE TAKEN ON PRIVATE ROAD !!!!!" src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622254-1DA5EC9400000578-269_87x84.jpg">
                <strong>'It's just a storm in a teacup - it was more like a drunken kiss': Husband plays down wife's 'sexual affair'...</strong>
              </a>
            </div>
            <a class="comment-count" href="/news/article-2622254/Katie-Price-brands-Jane-Pountney-homewrecker-husband-Derrick-plays-affair.html#comments">
              <b class="ico"></b>
        
        Comments (1,858)
            </a>
          </li>
          <li class="news">
            <div class="link-bow linkro-ccogr2">
              <a href="/news/article-2622809/Mother-strangled-two-babies-death-suffering-postnatal-depression-returns-1-5m-mansion-Nappy-valley-two-years-later-release-mental-hospital.html">
                <img alt="Felicity Boots, 36, who killed her two children while suffering from postnatal depression, has been spotted out and about in Wandsworth, London, with her banker husband Jeff, 36, two years after the tragedy" src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622809-1DA5574200000578-375_87x84.jpg">
                <strong>Mother who killed her two babies while suffering post-natal depression returns after two years to £1.5million...</strong>
              </a>
            </div>
            <a class="comment-count" href="/news/article-2622809/Mother-strangled-two-babies-death-suffering-postnatal-depression-returns-1-5m-mansion-Nappy-valley-two-years-later-release-mental-hospital.html#comments">
              <b class="ico"></b>
        
        Comments (1,073)
            </a>
          </li>
          <li class="debate">
            <div class="link-bow linkro-ccogr2">
              <a href="/debate/article-2622948/STEPHEN-GLOVER-The-Clarkson-racism-row-shows-touch-liberal-bullies-real-world.html">
                <img alt="Top Gear, which features Richard Hammond, left, Jeremy Clarkson, centre, and James May, right, 'is not really about cars. It is about Jeremy Clarkson - striking poses, challenging received wisdom, being rude, accepting (and making) daft and often infantile challenges.'" src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1A8AFAA9000005DC-326_87x84.jpg">
                <strong>STEPHEN GLOVER: The Clarkson 'racism' row shows how out of touch liberal bullies are with the real world</strong>
              </a>
            </div>
            <a class="comment-count" href="/debate/article-2622948/STEPHEN-GLOVER-The-Clarkson-racism-row-shows-touch-liberal-bullies-real-world.html#comments">
              <b class="ico"></b>
        
        Comments (1,071)
            </a>
          </li>
          <li class="tvshowbiz">
            <div class="link-bow linkro-ccogr2">
              <a href="/tvshowbiz/article-2623245/Lily-Allen-shares-snap-drip-saying-down.html">
                <img alt="Lily Allens sparked concern from her fans on Twitter after she posted a snap of herself in hospital" src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623245-1DAA7B5E00000578-814_87x84.jpg">
                <strong>'Sheezus in Shospital': Lily Allen shares snap of herself ill on a drip as she reveals that she 'can't keep...</strong>
              </a>
            </div>
            <a class="comment-count" href="/tvshowbiz/article-2623245/Lily-Allen-shares-snap-drip-saying-down.html#comments">
              <b class="ico"></b>
        
        Comments (1,009)
            </a>
          </li>
        </ul>
      </div>
      <div >
        <div class="xogr2">
          <select class="dropdown">
            <option value="all" selected data-url="/api/sm/most_commented_articles/all/gb">All Channels</option>
            <option value="news" data-url="/api/sm/most_commented_articles/news/gb">News</option>
            <option value="tvshowbiz" data-url="/api/sm/most_commented_articles/tvshowbiz/gb">TV &amp; Showbiz</option>
            <option value="sport" data-url="/api/sm/most_commented_articles/sport/gb">Sport</option>
            <option value="femail" data-url="/api/sm/most_commented_articles/femail/gb">Femail</option>
            <option value="health" data-url="/api/sm/most_commented_articles/health/gb">Health</option>
            <option value="money" data-url="/api/sm/most_commented_articles/money/gb">Money</option>
            <option value="sciencetech" data-url="/api/sm/most_commented_articles/sciencetech/gb">Science</option>
            <option value="travel" data-url="/api/sm/most_commented_articles/travel/gb">Travel</option>
          </select>
        </div>
        <ul class="lb-article">
          <li class="news first">
            <div class="link-bow linkro-ccogr2">
              <a href="/news/article-2623127/Can-pass-salt-Mr-President-Obama-rubs-shoulders-Spielberg-Kim-The-Boss-star-studded-L-A-fundraiser.html">
                <img alt="obama preview" src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA9F4D800000578-887_308x185.jpg">
                <strong>Can you pass the salt, Mr President? Obama rubs shoulders with Spielberg, Kim...</strong>
              </a>
            </div>
            <a class="comment-count" href="/news/article-2623127/Can-pass-salt-Mr-President-Obama-rubs-shoulders-Spielberg-Kim-The-Boss-star-studded-L-A-fundraiser.html#comments">
              <b class="ico"></b>
        
        Comments (304)
            </a>
          </li>
          <li class="tvshowbiz">
            <div class="link-bow linkro-ccogr2">
              <a href="/tvshowbiz/article-2622986/Kim-Kardashian-reveals-lengthy-post-fears-raising-mixed-race-daughter-North-West.html">
                <img alt="'Racism is still alive': Kim Kardashian reveals her serious side as she blogs about her fears over raising a mixed-race child" src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622986-1DAAB9E600000578-845_87x84.jpg">
                <strong>'Racism is still alive': Kim Kardashian reveals her serious side as she blogs about her fears over raising a...</strong>
              </a>
            </div>
            <a class="comment-count" href="/tvshowbiz/article-2622986/Kim-Kardashian-reveals-lengthy-post-fears-raising-mixed-race-daughter-North-West.html#comments">
              <b class="ico"></b>
        
        Comments (291)
            </a>
          </li>
          <li class="news">
            <div class="link-bow linkro-ccogr2">
              <a href="/news/article-2622451/Three-dead-raging-fire-retired-tennis-star-James-Blakes-Florida-mansion-victims-heavy-duty-fireworks-strapped-heads.html">
                <img alt="Retired: Blake, pictured, is a former professional tennis player, who at one point was the #1-ranked American in the world. He retired from the court last year" src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622451-1DA56EB800000578-987_87x84.jpg">
                <strong>Former executive, his wife and two children found dead 'with heavy duty FIREWORKS strapped to their heads'...</strong>
              </a>
            </div>
            <a class="comment-count" href="/news/article-2622451/Three-dead-raging-fire-retired-tennis-star-James-Blakes-Florida-mansion-victims-heavy-duty-fireworks-strapped-heads.html#comments">
              <b class="ico"></b>
        
        Comments (245)
            </a>
          </li>
          <li class="news">
            <div class="link-bow linkro-ccogr2">
              <a href="/news/article-2622708/One-ten-Americans-believe-space-aliens-involved-disappearance-ill-fated-Malaysian-flight-MH370.html">
                <img alt="Disappeared: The Malaysia Airlines Boeing 777 which vanished almost two months ago without trace" src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622708-1C449ECA00000578-687_87x84.jpg">
                <strong>One in ten Americans believe 'space aliens' were involved in the disappearance of ill-fated Malaysian flight...</strong>
              </a>
            </div>
            <a class="comment-count" href="/news/article-2622708/One-ten-Americans-believe-space-aliens-involved-disappearance-ill-fated-Malaysian-flight-MH370.html#comments">
              <b class="ico"></b>
        
        Comments (244)
            </a>
          </li>
          <li class="news">
            <div class="link-bow linkro-ccogr2">
              <a href="/news/article-2622432/Lynne-Cheney-argues-Monica-Lewinskys-tell-article-Hillary-Clintons-presidential-plan.html">
                <img alt="Monica Lewinsky, now 40, said that she has decided to not wait in the shadows for fear of derailing Hillary Clinton's expected presidential run in 2016" src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622432-1DA6341700000578-915_87x84.jpg">
                <strong>The Clintons' plot: Lynne Cheney claims Monica Lewinsky's tell-all could be part of Hillary's White House...</strong>
              </a>
            </div>
            <a class="comment-count" href="/news/article-2622432/Lynne-Cheney-argues-Monica-Lewinskys-tell-article-Hillary-Clintons-presidential-plan.html#comments">
              <b class="ico"></b>
        
        Comments (207)
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>


  </div>

        <div class="item arrow_feel_good_wrapper">
    <div class='lb-tabbed-pane arrow-trend'>
    <h2 class='lb-hdr'>ARROW FEEL-GOOD FACTOR</h2>
    <ul class='lb-tabs cleared'>
      <li class='selected-tab first'>24 hours</li>
      <li >7 days</li>
      <li >30 days</li>
    </ul>
    <p class='xogr2'>Total of votes up and down</p>
    <div class='lb-panes'>
      <div class='arrow-groups selected-pane'>
        <ul class='cleared'>
          <li>
            <span class='lb-arr-l up'></span>
            <span class='rating-positive'>2,851,779</span>
          </li>
          <li class='last'>
            <span class='lb-arr-l down'></span>
            <span class='rating-negative'>804,525</span>
          </li>
        </ul>
        <div class='lb-stats'>
          <div class='gr4'>Overall trend</div>
          <div class='rating-positive'>2,047,254</div>
          <div class='lb-arr-l up'></div>
        </div>
      </div>
      <div class='arrow-groups '>
        <ul class='cleared'>
          <li>
            <span class='lb-arr-l up'></span>
            <span class='rating-positive'>17,545,411</span>
          </li>
          <li class='last'>
            <span class='lb-arr-l down'></span>
            <span class='rating-negative'>4,783,103</span>
          </li>
        </ul>
        <div class='lb-stats'>
          <div class='gr4'>Overall trend</div>
          <div class='rating-positive'>12,762,308</div>
          <div class='lb-arr-l up'></div>
        </div>
      </div>
      <div class='arrow-groups '>
        <ul class='cleared'>
          <li>
            <span class='lb-arr-l up'></span>
            <span class='rating-positive'>69,704,738</span>
          </li>
          <li class='last'>
            <span class='lb-arr-l down'></span>
            <span class='rating-negative'>19,364,132</span>
          </li>
        </ul>
        <div class='lb-stats'>
          <div class='gr4'>Overall trend</div>
          <div class='rating-positive'>50,340,606</div>
          <div class='lb-arr-l up'></div>
        </div>
      </div>
    </div>
  </div>


  </div>

        <div class="sciencetech item">
    <div class="editors-choice ccox link-ccox linkro-darkred" id="p-1511"
       data-track-module="llg-1000258^editors_choice">
    <h3 class="bdrcc">THE BEST OF THE WEB - DIGESTED </h3>
    <ul class="cleared">
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://www.todayifoundout.com/index.php/2014/01/planes-ships-used-word-mayday-distress/" target="_blank"
           >Why do ships and planes call Mayday in distress?</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://time.com/85017/ending-afghanistans-drug-addiction-is-looking-like-mission-implausible/?utm_source=feedburner&amp;utm_medium=feed&amp;utm_campaign=Feed%3A+timeblogs%2Fswampland+%28TIME%3A+Swampland%29" target="_blank"
           >Afghanistan's drug addiction is going to be impossible to kick</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://www.nytimes.com/2014/05/04/us/when-hitting-find-my-iphone-takes-you-to-a-thiefs-doorstep.html?hp" target="_blank"
           >Should you confront a thief who's stolen your phone?</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://www.thedatereport.com/dating/love/inside-the-secret-sexual-matriarchy-of-iran/" target="_blank"
           >Iran's rampant secret sex orgies and the WOMEN who love them</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://www.bbc.co.uk/news/business-27253103" target="_blank"
           >Why are household appliances getting less reliable than ever?</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://www.nature.com/news/you-don-t-always-know-what-you-re-saying-1.15136" target="_blank"
           >Why we don't always know what we've actually said</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://tech.fortune.cnn.com/2014/05/01/kill-the-password-and-the-pin-number-and-the-car-key/" target="_blank"
           >Could this be in end of PINs and passwords?</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://www.theatlantic.com/health/archive/2014/05/nearsightedness-and-the-indoor-life/361169/" target="_blank"
           >Why modern life has made near-sightedness soar</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://qz.com/205478/your-next-iphone-might-be-delivered-from-china-via-a-2000-year-old-trade-route/" target="_blank"
           >The return of the Silk Route</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://www.gq.com/entertainment/movies-and-tv/201405/horrible-bosses-hollywood" target="_blank"
           >Why there's nothing funny about working for a Hollywood comedy writer</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://theweek.com/article/index/260535/are-teen-pregnancies-good-for-the-economy" target="_blank"
           >Are teenage pregnancies good for an economy?</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://www.washingtonpost.com/blogs/innovations/wp/2014/04/28/heres-what-it-actually-takes-to-make-it-as-an-entrepreneur/" target="_blank"
           >What it really takes to make it as an entreprenuer</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://gizmodo.com/why-smartphones-are-about-to-get-tacky-as-hell-1567823389" target="_blank"
           >Why mobile phones are about to go bling</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://theweek.com/article/index/99512/he-said-he-was-leaving-she-ignored-him" target="_blank"
           >The wife who simply ignored her husband when he said he wanted to leave</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://www.mensjournal.com/magazine/building-a-bigger-action-hero-20140418" target="_blank"
           >How modern action heroes keep getting buffer and bigger</a>
      </li>
      <li>
        <div class="wocc">&nbsp;</div>
        <a class="js-tl" href="http://www.newyorker.com/online/blogs/elements/2014/04/what-makes-an-alien-intelligent.html" target="_blank"
           >What makes an alien intelligent?</a>
      </li>
    </ul>
  </div>
  </div>
  <script type="text/javascript">
    DM.has('p-1511', 'comScore', {
      mo_mod_id: '1000258',
      mo_mod_pos: 'p-1511'
    });
  </script>
  <script type="text/javascript">
      DM.has('p-1511', 'externalLinkTracker');
  </script>
  </div>
  </div>
    <div class="gamma">
        <div class="item video">
    <div class="video video_carousel_container cleared" id="p-1514"
       data-track-module="llg-62027998^video_mosaic" data-track-selector=".videoLink" data-track-type="cl">
    <div class="video_carousel_title bdrcc">
      <div class="wocc carousel-title" style="text-transform: uppercase;">video</div>
      <img src="http://i.dailymail.co.uk/i/furniture/standard_modules/video/icon_filmstrip.png">
      <div class="channel-title" style="text-transform: uppercase;">Watch Editor's Top Picks...</div>
      <div class="rotator-title">
        <ul class="rotator-pages">
          <li class="linkro-wocc link-wocc">
            <a href="#" data-page="1"><span class="usability">1</span></a>
          </li>
          <li class="linkro-wocc link-wocc">
            <a href="#" data-page="2"><span class="usability">2</span></a>
          </li>
          <li class="linkro-wocc link-wocc">
            <a href="#" data-page="3"><span class="usability">3</span></a>
          </li>
          <li class="linkro-wocc link-wocc">
            <a href="#" data-page="4"><span class="usability">4</span></a>
          </li>
          <li class="linkro-wocc link-wocc">
            <a href="#" data-page="5"><span class="usability">5</span></a>
          </li>
          <li class="linkro-wocc link-wocc">
            <a href="#" data-page="6"><span class="usability">6</span></a>
          </li>
        </ul>
      </div>
    </div>
    <div id="video_linklist">
      <div class="link-wox linkro-ccox left">
        <a class="js-move-prev" href="#">
          <div class="left_scroll"><span></span></div>
        </a>
      </div>
      <div class="rotator link-ccob linkro-wocc">
        <ul class="js-itemList rotator-panels large_video">
          <li>
            <a class="videoLink" href="/video/sciencetech/video-1093939/Adorable-footage-Ralphee-kitten-born-cerebellar-hypoplasia-inseparable-Max-dog.html"
               data-videoid="3543351818001"
               data-source="YouTube"
               data-modal-type="video-lightbox"
               data-target="/api/video-carousel.html?video-id=1093939&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
               data-channel="sciencetech">
              <span class="wocc">
                <div class="playbtn"></div>Watch video
              </span>
              <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA4348A00000578-511_636x358.jpg">
              <div class="video-item-time"><p>84289</p></div>
              <div class="video-item-title bdrcc wob">Adorable footage, Ralphee the kitten born with cerebellar hypoplasia is inseparable from Max the dog</div>
            </a>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/news/video-1094053/The-Un-credible-shrinking-man.html"
                   data-videoid="3546032775001"
                   data-source="Other"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1094053&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA9B90E00000578-169_636x358.jpg">
                  <div class="video-item-time"><p>225025</p></div>
                  <div class="video-item-title bdrcc wob">The Un-credible shrinking man</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093965/tooth-extracted-self-hypnosis.html"
                   data-videoid="3543673450001"
                   data-source="Other"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093965&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA5300500000578-769_636x358.jpg">
                  <div class="video-item-time"><p>566521</p></div>
                  <div class="video-item-title bdrcc wob">tooth extracted under self hypnosis</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1094057/Police-body-cam-action.html"
                   data-videoid="3546054295001"
                   data-source="Police"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1094057&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA9DB6F00000578-70_636x358.jpg">
                  <div class="video-item-time"><p>35968</p></div>
                  <div class="video-item-title bdrcc wob">Police body cam in action</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093905/Notorious-gangster-giant-ferris-wheel.html"
                   data-videoid="3543291933001"
                   data-source="MEN"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093905&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA2C71000000578-877_636x358.jpg">
                  <div class="video-item-time"><p>81665</p></div>
                  <div class="video-item-title bdrcc wob">Notorious gangster on giant ferris wheel</div>
                </a>
              </li>
            </ul>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/news/video-1093953/Mini-tornado-strikes-WORCESTER.html"
                   data-videoid="3543417137001"
                   data-source="SWNS"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093953&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA4A0A000000578-7_636x358.jpg">
                  <div class="video-item-time"><p>45001</p></div>
                  <div class="video-item-title bdrcc wob">Mini-tornado strikes in WORCESTER</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/sciencetech/video-1093915/New-spray-lets-people-ERASE-DNA.html"
                   data-videoid="3543334799001"
                   data-source="Vimeo"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093915&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="sciencetech">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA429EC00000578-458_636x358.jpg">
                  <div class="video-item-time"><p>107555</p></div>
                  <div class="video-item-title bdrcc wob">New spray lets people ERASE their DNA!</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093863/Police-dog-grabs-man-neck.html"
                   data-videoid="3543202396001"
                   data-source="SWNS"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093863&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA22C4F00000578-166_636x358.jpg">
                  <div class="video-item-time"><p>24521</p></div>
                  <div class="video-item-title bdrcc wob">Police dog grabs man by the neck</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093891/Stowaway-teen-drops-plane.html"
                   data-videoid="3543174854001"
                   data-source="Reuters"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093891&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA2094D00000578-83_636x358.jpg">
                  <div class="video-item-time"><p>82176</p></div>
                  <div class="video-item-title bdrcc wob">Stowaway teen drops out of plane</div>
                </a>
              </li>
            </ul>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/femail/video-1093888/Worlds-tallest-teenager-fiance.html"
                   data-videoid="3543152558001"
                   data-source="Barcroft"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093888&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="femail">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA1E9FD00000578-680_636x358.jpg">
                  <div class="video-item-time"><p>212301</p></div>
                  <div class="video-item-title bdrcc wob">World's tallest teenager and her fiance</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093768/Mans-McDonalds-memorabilia-collection.html"
                   data-videoid="3541106244001"
                   data-source="Barcroft"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093768&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/06/video-undefined-1D9D812400000578-459_636x358.jpg">
                  <div class="video-item-time"><p>136836</p></div>
                  <div class="video-item-title bdrcc wob">Man's McDonalds memorabilia collection</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/tvshowbiz/video-1093565/Half-dressed-Harry-Styles-Niall-Horan.html"
                   data-videoid="3538071209001"
                   data-source="YouTube"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093565&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="tvshowbiz">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/05/video-undefined-1D96AA3000000578-438_636x358.jpg">
                  <div class="video-item-time"><p>34459</p></div>
                  <div class="video-item-title bdrcc wob">Half-dressed Harry Styles and Niall Horan</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/femail/video-1093741/Meet-Britains-vainest-man.html"
                   data-videoid="3540722507001"
                   data-source="Barcroft"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093741&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="femail">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/06/video-undefined-1D9C559E00000578-360_636x358.jpg">
                  <div class="video-item-time"><p>136023</p></div>
                  <div class="video-item-title bdrcc wob">Meet Britain's vainest man</div>
                </a>
              </li>
            </ul>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/news/video-1093560/Ray-Winstone---20-years-Ford-Mondeo.html"
                   data-videoid="3537461949001"
                   data-source="YouTube"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093560&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/05/video-undefined-1D95B1D200000578-522_636x358.jpg">
                  <div class="video-item-time"><p>365645</p></div>
                  <div class="video-item-title bdrcc wob">Ray Winstone - '20 years of Ford Mondeo'</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093722/Animation-shows-Piccadilly-Circus-1960.html"
                   data-videoid="3540671472001"
                   data-source="Other"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093722&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/06/video-undefined-1D9B511C00000578-64_636x358.jpg">
                  <div class="video-item-time"><p>46400</p></div>
                  <div class="video-item-title bdrcc wob">Animation shows Piccadilly Circus in 1960</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093606/Pistorius-neighbour-takes-stand.html"
                   data-videoid="3538143559001"
                   data-source="Reuters"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093606&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/05/video-undefined-1D96B19700000578-428_636x358.jpg">
                  <div class="video-item-time"><p>225211</p></div>
                  <div class="video-item-title bdrcc wob">Pistorius' neighbour takes stand</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093386/Man-knocked-dragged-GHOST.html"
                   data-videoid="3532836293001"
                   data-source="YouTube"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093386&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/03/video-undefined-1D8A3AA600000578-59_636x358.jpg">
                  <div class="video-item-time"><p>60512</p></div>
                  <div class="video-item-title bdrcc wob">Man  knocked over and dragged by a GHOST</div>
                </a>
              </li>
            </ul>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/news/video-1093500/Furby-kitten-plays-DJ-decks.html"
                   data-videoid="3535209748001"
                   data-source="Getty"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093500&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/04/video-undefined-1D905DA200000578-415_636x358.jpg">
                  <div class="video-item-time"><p>54823</p></div>
                  <div class="video-item-title bdrcc wob">Furby the kitten plays the DJ decks</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093457/Obamas-hillarious-dinner-speech.html"
                   data-videoid="3534986261001"
                   data-source="Reuters"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093457&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/04/video-undefined-1D8FAEA900000578-408_636x358.jpg">
                  <div class="video-item-time"><p>194769</p></div>
                  <div class="video-item-title bdrcc wob">Obama's hillarious dinner speech</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/tvshowbiz/video-1093415/Kendra-Wilkinson-bright-pink-top.html"
                   data-videoid="3533082775001"
                   data-source="Splash"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093415&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="tvshowbiz">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/03/video-undefined-1D8AF99800000578-797_636x358.jpg">
                  <div class="video-item-time"><p>89931</p></div>
                  <div class="video-item-title bdrcc wob">Kendra Wilkinson in bright pink top</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093171/Clarksons-response-n-word-video.html"
                   data-videoid="3527926890001"
                   data-source="Other"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093171&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D8187A300000578-983_636x358.jpg">
                  <div class="video-item-time"><p>98244</p></div>
                  <div class="video-item-title bdrcc wob">Clarkson's response to n-word video</div>
                </a>
              </li>
            </ul>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/news/video-1093226/Party-Princes-eat-BBQ-Memphis.html"
                   data-videoid="3529937971001"
                   data-source="Splash"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093226&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/02/video-undefined-1D84418600000578-941_636x358.jpg">
                  <div class="video-item-time"><p>67547</p></div>
                  <div class="video-item-title bdrcc wob">Party Princes eat BBQ in Memphis</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/travel/video-1093161/Fly-Thunderbirds.html"
                   data-videoid="3527616667001"
                   data-source="Other"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093161&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="travel">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D80C48400000578-25_636x358.jpg">
                  <div class="video-item-time"><p>149955</p></div>
                  <div class="video-item-title bdrcc wob">Fly with the Thunderbirds</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093165/Shark-shuts-beaches-Australia.html"
                   data-videoid="3527807711001"
                   data-source="Reuters"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093165&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D816D0F00000578-724_636x358.jpg">
                  <div class="video-item-time"><p>60628</p></div>
                  <div class="video-item-title bdrcc wob">Shark shuts beaches in Australia</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093058/Nigel-Farage-gets-hit-Egg.html"
                   data-videoid="3527384080001"
                   data-source="Other"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093058&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D806C8E00000578-450_636x358.jpg">
                  <div class="video-item-time"><p>40008</p></div>
                  <div class="video-item-title bdrcc wob">Nigel Farage gets hit by an Egg</div>
                </a>
              </li>
            </ul>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/news/video-1093162/Camilla-bids-farewell-brother-Mark.html"
                   data-videoid="3527649976001"
                   data-source="PA"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093162&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D80BCF900000578-364_636x358.jpg">
                  <div class="video-item-time"><p>165792</p></div>
                  <div class="video-item-title bdrcc wob">Camilla bids farewell to her brother Mark</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093139/Incredible-all-star-celeb-proposal.html"
                   data-videoid="3527189692001"
                   data-source="Caters"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093139&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D7FFF6E00000578-728_636x358.jpg">
                  <div class="video-item-time"><p>49923</p></div>
                  <div class="video-item-title bdrcc wob">Incredible all-star celeb proposal</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/travel/video-1093161/FLY-Thunderbirds.html"
                   data-videoid="3527616667001"
                   data-source="Other"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093161&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="travel">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D80C48400000578-25_636x358.jpg">
                  <div class="video-item-time"><p>149955</p></div>
                  <div class="video-item-title bdrcc wob">FLY with the Thunderbirds!</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093092/Bizarre-video-snake-eating-ITSELF.html"
                   data-videoid="3526894070001"
                   data-source="YouTube"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093092&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D7EAAFD00000578-810_636x358.jpg">
                  <div class="video-item-time"><p>110017</p></div>
                  <div class="video-item-title bdrcc wob">Bizarre video of snake eating ITSELF!</div>
                </a>
              </li>
            </ul>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/news/video-1093151/Stun-grenades-used-Donetsk-clashes.html"
                   data-videoid="3527425392001"
                   data-source="AP"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093151&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D806C1000000578-735_636x358.jpg">
                  <div class="video-item-time"><p>120032</p></div>
                  <div class="video-item-title bdrcc wob">Stun grenades used in Donetsk clashes</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093085/Allegations-racism-surround-Clarkson.html"
                   data-videoid="3526790882001"
                   data-source="Other"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093085&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D7E2FE300000578-265_636x358.jpg">
                  <div class="video-item-time"><p>14281</p></div>
                  <div class="video-item-title bdrcc wob">Allegations of racism surround Clarkson</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093131/Hero-cop-pulls-man-burning-car.html"
                   data-videoid="3527094949001"
                   data-source="Facebook"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093131&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D7FAC4300000578-277_636x358.jpg">
                  <div class="video-item-time"><p>41936</p></div>
                  <div class="video-item-title bdrcc wob">Hero cop pulls man from burning car</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/tvshowbiz/video-1093147/Teenage-Mutant-Ninja-Turtles-new-trailer.html"
                   data-videoid="3527384024001"
                   data-source="YouTube"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093147&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="tvshowbiz">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D80500C00000578-971_636x358.jpg">
                  <div class="video-item-time"><p>100218</p></div>
                  <div class="video-item-title bdrcc wob">Teenage Mutant Ninja Turtles new trailer</div>
                </a>
              </li>
            </ul>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/news/video-1092900/Two-men-FIGHT-tube.html"
                   data-videoid="3522604313001"
                   data-source="YouTube"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1092900&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/04/30/video-undefined-1D78ECDF00000578-629_636x358.jpg">
                  <div class="video-item-time"><p>80272</p></div>
                  <div class="video-item-title bdrcc wob">Two men FIGHT on the tube</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/tvshowbiz/video-1093003/Is-THIS-Kim-K-wedding-dress-shopping.html"
                   data-videoid="3524789410001"
                   data-source="Other"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093003&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="tvshowbiz">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/04/30/video-undefined-1D7B37C200000578-876_636x358.jpg">
                  <div class="video-item-time"><p>59606</p></div>
                  <div class="video-item-title bdrcc wob">Is THIS Kim K wedding dress shopping?</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1093087/Motorist-mows-12-year-old-cyclist.html"
                   data-videoid="3526829879001"
                   data-source="Solent News &amp; Pictures"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093087&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D7E775500000578-647_636x358.jpg">
                  <div class="video-item-time"><p>52431</p></div>
                  <div class="video-item-title bdrcc wob">Motorist mows down a 12-year-old cyclist</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/femail/video-1092997/Priceless-reaction-Moms-baby-news.html"
                   data-videoid="3524394400001"
                   data-source="YouTube"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1092997&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="femail">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/04/30/video-undefined-1D7AB7E700000578-386_636x358.jpg">
                  <div class="video-item-time"><p>106720</p></div>
                  <div class="video-item-title bdrcc wob">Priceless reaction to Mom's baby news</div>
                </a>
              </li>
            </ul>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/tvshowbiz/video-1093091/BEST-celeb-photobombs-EVER.html"
                   data-videoid="3526894063001"
                   data-source="US TV"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1093091&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="tvshowbiz">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/05/01/video-undefined-1D7EAF0C00000578-920_636x358.jpg">
                  <div class="video-item-time"><p>154048</p></div>
                  <div class="video-item-title bdrcc wob">BEST celeb photobombs EVER?</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1092929/High-speed-chase-suspect-tries-grab-gun.html"
                   data-videoid="3522827650001"
                   data-source="MI9"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1092929&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/04/30/video-undefined-1D79A74400000578-167_636x358.jpg">
                  <div class="video-item-time"><p>211480</p></div>
                  <div class="video-item-title bdrcc wob">High speed chase suspect tries to grab gun</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1092661/Clinging-taxi-doing-60-MPH.html"
                   data-videoid="3517623963001"
                   data-source="MailOnline"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1092661&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/04/28/video-undefined-1D6F32B800000578-275_636x358.jpg">
                  <div class="video-item-time"><p>200853</p></div>
                  <div class="video-item-title bdrcc wob">Clinging to a taxi doing 60 MPH</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1092914/Naked-drunk-man-tasered-police.html"
                   data-videoid="3522670892001"
                   data-source="SWNS"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1092914&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/04/30/video-undefined-1D77D80400000578-881_636x358.jpg">
                  <div class="video-item-time"><p>36758</p></div>
                  <div class="video-item-title bdrcc wob">Naked drunk man tasered by police</div>
                </a>
              </li>
            </ul>
          </li>
          <li>
            <ul class="medium_video">
              <li>
              <a class="videoLink" href="/video/news/video-1092960/Lorry-plundered-men-MOVING-CAR.html"
                   data-videoid="3522948289001"
                   data-source="YouTube"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1092960&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/04/30/video-undefined-1D78B0DC00000578-263_636x358.jpg">
                  <div class="video-item-time"><p>71936</p></div>
                  <div class="video-item-title bdrcc wob">Lorry plundered by men from MOVING CAR</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1092862/Bloated-whale-causes-unease.html"
                   data-videoid="3521808860001"
                   data-source="Reuters"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1092862&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/04/30/video-undefined-1D75B19A00000578-637_636x358.jpg">
                  <div class="video-item-time"><p>56030</p></div>
                  <div class="video-item-title bdrcc wob">Bloated whale causes unease</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/femail/video-1092887/Bling-Flawless-BLUE-diamond-grabs.html"
                   data-videoid="3522537140001"
                   data-source="AP"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1092887&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="femail">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/04/30/video-undefined-1D7787AB00000578-612_636x358.jpg">
                  <div class="video-item-time"><p>329236</p></div>
                  <div class="video-item-title bdrcc wob">Bling! Flawless BLUE diamond up for grabs</div>
                </a>
              </li>
              <li>
              <a class="videoLink" href="/video/news/video-1092894/Violent-clashes-spark-chaos-Kiev.html"
                   data-videoid="3522390012001"
                   data-source="AP"
                   data-modal-type="video-lightbox"
                   data-target="/api/video-carousel.html?video-id=1092894&amp;colour=video&amp;item-type=ll&amp;item-id=62027998 .video-lightbox"
                   data-channel="news">
                  <span class="wocc">
                    <div class="playbtn"></div>Watch video
                  </span>
                  <img src="http://i.dailymail.co.uk/i/pix/2014/04/30/video-undefined-1D7747AD00000578-533_636x358.jpg">
                  <div class="video-item-time"><p>43259</p></div>
                  <div class="video-item-title bdrcc wob">Violent clashes spark chaos in Kiev</div>
                </a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="link-wox linkro-ccox right">
        <a class="js-move-next" href="#">
          <div class="right_scroll"><span></span></div>
        </a>
      </div>
    </div>
    <script type="text/javascript">
  DM.has("p-1514", 'videoChannelCarouselModule',
         {"player" : "1989148206001",
          "playerKey" : "AQ~~,AAAAAFSL1bg~,CmS1EFtcMWELN_eSE9A7gpcGWF5XAVmI",
          "nonEmbeddablePlayerIdent" : "2572801325001",
          "nonEmbeddablePlayerKey" : "AQ~~,AAAAAFSL1bg~,CmS1EFtcMWF3nDd2YNUcSIWL0H_o4As-",
          "trackingType" : "video_mosaic",
          "channelShortName" : "video",
          "overlayType" : "carousel",
          "pageCount" : "6",
          "pageSize" : 2,
          "onPos": 0,
          "updateStyleOnHover": true,
          "videoPlayerConfigMap": {'3543351818001' : 'false','3546032775001' : 'false','3543673450001' : 'false','3546054295001' : 'false','3543291933001' : 'false','3543417137001' : 'false','3543334799001' : 'false','3543202396001' : 'false','3543174854001' : 'false','3543152558001' : 'false','3541106244001' : 'false','3538071209001' : 'false','3540722507001' : 'false','3537461949001' : 'false','3540671472001' : 'false','3538143559001' : 'false','3532836293001' : 'false','3535209748001' : 'false','3534986261001' : 'false','3533082775001' : 'false','3527926890001' : 'false','3529937971001' : 'false','3527616667001' : 'false','3527807711001' : 'false','3527384080001' : 'false','3527649976001' : 'false','3527189692001' : 'false','3527616667001' : 'false','3526894070001' : 'false','3527425392001' : 'false','3526790882001' : 'false','3527094949001' : 'false','3527384024001' : 'false','3522604313001' : 'false','3524789410001' : 'false','3526829879001' : 'false','3524394400001' : 'false','3526894063001' : 'false','3522827650001' : 'false','3517623963001' : 'false','3522670892001' : 'false','3522948289001' : 'false','3521808860001' : 'false','3522537140001' : 'false','3522390012001' : 'false','3521089765001' : 'false','3518653475001' : 'false'},
          "rsi" : typeof(adverts) != 'undefined' && typeof (adverts.getRsiValues) != 'undefined' ? adverts.getRsiValues() : null
  });
  </script>

  </div>

  </div>

  </div>
    <div class="cleared">
        <div class="alpha">
     <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline126}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2622999/Celebrities-join-campaign-bring-kidnapped-Nigerian-girls.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622999-1DAA77E000000578-489_636x382.jpg" height="382" width="636" alt="girls preview" />
        </a>
      <div >
       <p>
         
         Leona Lewis (left), Michelle Obama (centre), and Malala Yousafzai (right) are among those lending their support to the social media campaign, which is encouraging military intervention to recover the girls who were kidnapped from their school by Boko Haram rebels in north-east Nigeria.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2622999/Celebrities-join-campaign-bring-kidnapped-Nigerian-girls.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622999">         194</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2622999/Celebrities-join-campaign-bring-kidnapped-Nigerian-girls.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/Rt7tHu| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622999-1DAA77E000000578-254_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline127}}</a>
    </h2>
    <div class="articletext">
      <a href="/travel/article-2622591/Best-food-travel-photos-world-Globetrotter-snaps-global-street-food.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-2622591-1DA5EDCB00000578-780_154x115.jpg" height="84" width="112" alt="Perfect pastry: Nick enjoyed a sweet snack while strolling along the historic streets of Amsterdam" />
      </a>
      <p>
        
        Nick Mollberg's holiday snaps will certainly make your mouth water. The consultant travels the world and always snaps local delicacies in front of an iconic view.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="travelmail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/travel/article-2622591/Best-food-travel-photos-world-Globetrotter-snaps-global-street-food.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622591">          12</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mEOsAd| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622591-1DA6065900000578-538_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline128}}</a>
    </h2>
    <div class="articletext">
      <a href="/travel/article-2623203/Wish-The-golden-age-American-travel-revealed-enchanting-collection-vintage-postcards.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623203-1DA9F5ED00000578-476_154x115.jpg" height="84" width="112" alt="Romping on the Beach at Coney Island" />
      </a>
      <p>
        
        The Boston Public Library has released a collection of 25,000 vintage postcards.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="travelmail">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/travel/article-2623203/Wish-The-golden-age-American-travel-revealed-enchanting-collection-vintage-postcards.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623203">           6</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtZ7PS| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623203-1DAAE5D500000578-908_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline129}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623086/Journalists-attack-table-destroy-set-live-television-crisis-Syria.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA9706000000578-690_154x115.jpg" height="84" width="112" alt="Total chaos: Jordanian TV guests destroy the 7 stars news studio and desk during live show" />
      </a>
      <p>
        
        Journalists Shaker Al-Johari and Mohammed Al-Jayousi were discussing the crisis in Syria when they disagreed about an issue and began hurling abuse at each other on TV channel 7 Stars.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623086/Journalists-attack-table-destroy-set-live-television-crisis-Syria.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623086">          24</span>)
      </span>
    </a>
  </li>

      <li class="">
    <a class="videos-link" href="/news/article-2623086/Journalists-attack-table-destroy-set-live-television-crisis-Syria.html#video" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Videos
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RtBU0n| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1DA9967B00000578-759_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

          <div class="article article-small">
    <h2 class="linkro-darkred"><a href="#">{{headline130}}</a>
    </h2>
    <div class="articletext">
      <a href="/news/article-2623049/Coney-Island-state-mind-Photos-Brooklyns-famed-beach-1960s-offer-intimate-look-sun-worshipers-no-inhibitions.html" class="js-link-clickable">
          <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623049-1D9216DE00000578-733_154x115.jpg" height="84" width="112" alt="The Brooklyn grandmother was not afraid in the least to show her decolletage" />
      </a>
      <p>
        
        In Aaron Rose's photographs taken in 1961-1963 on Coney island, Brooklyn's egalitarian beach emerges as a human melting pot where sunbathers of every race and body type were welcome.
      </p>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623049/Coney-Island-state-mind-Photos-Brooklyns-famed-beach-1960s-offer-intimate-look-sun-worshipers-no-inhibitions.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623049">          99</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1mErObr| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623049-1DA9602C00000578-939_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>

    </div>
    <div class="column-split">
          <div class="article article-large cleared">
    <h2 class="linkro-darkred"><a href="#">{{headline131}}</a>
    </h2>
    <a href="/news/article-2622896/Mac-GPs-charging-patients.html">
        <img  src="http://i.dailymail.co.uk/i/pix/2014/05/07/article-0-1DA6448D00000578-793_308x185.jpg" height="185" width="308" alt="'Thank you Mr Spiggot. I'd like to check on that sore toe again this afternoon, three times next week and I'll pay you a home visit next month.'" />
    </a>
    <div class="articletext-holder">
      <p>
        
        'Thank you Mr Spiggot. I'd like to check on that sore toe again this afternoon, three times next week and I'll pay you a home visit next month.'
      </p>
      <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2622896/Mac-GPs-charging-patients.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2622896">          23</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/1iownmd| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/07/article-0-1DA6448D00000578-727_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

    </div>
  </div>


    </div>
  </div>

     <div class="column-splitter">
    <div class="column-split first-column">
    </div>
    <div class="column-split">
    </div>
  </div>
    <div class="article article-tri-headline">
    <h2 class="linkro-darkred"><a href="#">{{headline132}}</a>
    </h2>
    <div class="articletext">
        <a href="/news/article-2623284/The-17th-Century-hand-painted-800-page-book-listed-EVERY-colour-reveals-actually-87-shades-grey.html">
            <img  src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623284-1DAB17BB00000578-43_636x382.jpg" height="382" width="636" alt="The book detailing every colour imaginable" />
        </a>
      <div >
       <p>
         
         The guide created by an artist known only as A. Boogert shows exactly how to mix certain colours by just using water. The book begins each chapter with instructions on how to use each colour when painting and then how to create different shades of it. A book historian who translated part of the book believes it was the most comprehensive guide of its time.
       </p>
      </div>
    </div>
    <div class="article-icon-links-container" data-followbutton="MailOnline">
    <ul class="article-icon-links cleared">
      <li class="first">
    <a class="comments-link" href="/news/article-2623284/The-17th-Century-hand-painted-800-page-book-listed-EVERY-colour-reveals-actually-87-shades-grey.html#comments" rel="nofollow">
      <span class="icon"></span>
      <span class="linktext">
        Comments (<span class="readerCommentNo" rel="2623284">          11</span>)
      </span>
    </a>
  </li>

      <li class=" gr3ox">
    <a class="http://dailym.ai/RuaXK2| js-sl share-link" data-article-image="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623284-1DAB17BB00000578-43_636x382.jpg" href="#">
      <span class="icon"></span>
      <span class="linktext">
        Share
      </span>
    </a>
  </li>

    </ul>
  </div>

  </div>


  </div>

        <div class="beta">
        <div class="item mpu_wrapper">
    <div class="mpu adHolder molads_mpu_bottom_right" id="p-1601">
    <script type="text/javascript">
      adverts.addToArray({type:'300x250', pos:'mpu_bottom_right', adProbe:false});
    </script>
  </div>
  </div>

        <div class="sport item">
    <div class="puff cleared" id="p-1602"
       data-track-module="llg-1000118^puff">
    
    <span class="tl">&nbsp;</span>
    <span class="tr">&nbsp;</span>
    <h3 class="wocc">TOP SPORT STORIES</h3>
    <ul class="link-bogr2 linkro-wocc">
      <li>
        <a href="/sport/football/article-2622533/Brighton-vs-Derby-live-Championship-play-semi-final.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2622533-1DAD798700000578-203_154x115.jpg" height="115" width="154" alt="Brighton host Derby in the play-off semi-final" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            LIVE: Brighton vs Derby
            </strong>
            Follow coverage of the Championship play-offs as Brighton host Derby at the Amex Stadium in the first leg of their semi-final
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623625/Jose-Mourinho-fined-10-000-FA-comments-Chelseas-Sunderland-loss.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-0-1D7B824E00000578-361_154x115.jpg" height="115" width="154" alt="FA rap: Jose Mourinho was hit by a £10,000 fine" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Mourinho fined £10,000 by the FA for comments after Chelsea's defeat to Sunderland
            </strong>
            Jose Mourinho has been fined after his sarcastic appraisal of officials
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623348/Marcus-Rashford-caught-middle-Manchester-City-look-prise-Manchester-United-starlet-away.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623348-1DAB9C8C00000578-425_154x115.jpg" height="115" width="154" alt="Tug of war: Manchester City are keen to take starlet Marcus Rushford from neighbours Manchester United" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Rashford caught in the middle as Man City look to prise United starlet away from Old Trafford
            </strong>
            City look to lure United's Marcus Rashford away from Old Trafford
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623157/Arsene-Wenger-tells-Arsenal-fans-not-expect-signings-quickly-summer.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623157-1D92347D00000578-830_154x115.jpg" height="115" width="154" alt="Waiting game: Arsene Wenger has told supporters not to expect a rush of new signings this summer" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Wenger tells Arsenal fans not to expect quick signings this summer
            </strong>
            Arsene Wenger has told Arsenal fans there won't be a rush of early signings this summer
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623352/Diego-offered-Arsenal-Gunners-look-challenge-spot-season.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/linkListItem-0-0DE9D98C00000578-520_154x115.jpg" height="115" width="154" alt="On target: Deigo was on target for Atletico during their Europa League winning run in 2011-12" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Diego offered to Arsenal as the Gunners look to challenge for top spot next season
            </strong>
            Arsenal have been offered Atletico Madrid midfielder Diego
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/formulaone/article-2623309/Nico-Rosberg-says-louder-megaphone-engines-tested-Spanish-GP.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/linkListItem-0-1D6DAEBC00000578-250_154x115.jpg" height="115" width="154" alt="On track: Nico Rosberg claims louder Formula One engines will be tested in Barcelona next week" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Rosberg says louder 'megaphone' engines will be tested after Spanish Grand Prix
            </strong>
            Nico Rosberg claims louder Formula One engines are on their way
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623207/Steven-Gerrard-jokes-infamous-gaffe-We-dont-slips-away.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623207-1D66477500000578-506_154x115.jpg" height="115" width="154" alt="Slipping away: Steven Gerrard lost his footing to allow Demba Ba to score a vital goal at Anfield" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Gerrard jokes about infamous gaffe: 'We don't get too down when it slips away!'
            </strong>
            Steven Gerrard laughs at himself over his slip against Chelsea
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623367/Laurent-Blanc-signs-new-deal-French-champions-Paris-Saint-Germain.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623367-1DA89FCE00000578-370_154x115.jpg" height="115" width="154" alt="Staying on: Laurent Blanc has signed a contract extension at French Champions Paris St Germain" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Blanc signs new deal at French champions Paris Saint Germain
            </strong>
            PSG manager Laurent Blanc has signed a new deal with the reigning French Champions
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/boxing/article-2623126/Floyd-Mayweather-times-two-girls-race-count-100-000-bed.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623126-1DA98F9100000578-304_154x115.jpg" height="115" width="154" alt="Splashing out: Mayweather times two girls counting out $100,000 money on his bed" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Mayweather times two women to count out $100,000 on his bed
            </strong>
            Floyd Mayweather has flaunted his wealth by getting two women to count out $100,000
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/worldcup2014/article-2623267/Lukas-Podolski-Mesut-Ozil-Per-Mertesacker-named-Germany-strong-World-Cup-squad.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/1399547273539_Puff_Image_galleryImage_ozil_JPG.JPG" height="115" width="154" alt="ozil.JPG" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Podoloski, Ozil and Mertesacker in German World Cup squad
            </strong>
            Arsenal's Mesut Ozil, Lukas Podolski and Per Mertesacker make World Cup squad for Germany
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623325/Gus-Poyet-leave-Sunderland-keeping-Black-Cats-Premier-League.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623325-1DA7206100000578-644_154x115.jpg" height="115" width="154" alt="Uncertain: Gus Poyet could leave Sunderland this summer - despite keeping them club in the Premier League" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Poyet could leave Sunderland... even after keeping Black Cats in Premier League
            </strong>
            Sunderland are fighting to keep hold of miracle manager Gus Poyet&nbsp;
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623257/Sam-Allardyce-faces-SACK-West-Ham-despite-guiding-Premier-League-safety-again.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623257-1D8AF76100000578-269_154x115.jpg" height="115" width="154" alt="It's over: Sam Allardyce will be sacked by West Ham United after their game against Manchester City" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Allardyce faces SACK at West Ham... despite guiding them to Premier League safety again
            </strong>
            Sam Allardyce's final aim as West Ham boss is to derail City's title bid
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623240/Alan-Pardew-sad-Newcastle-supporters-calling-head.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623240-1D8C355600000578-712_154x115.jpg" height="115" width="154" alt="Not happy: Alan Pardew is saddened by Newcastle United supporters calling for his head as the club's manager" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Pardew 'sad' about Newcastle supporters calling for his head
            </strong>
            Newcastle boss Alan Pardew admits he has been saddened by calls from fans for his head
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623213/Diego-Simeone-believes-La-Liga-fans-want-Atletico-Madrid-beat-Barcelona-Real-Madrid-title.html">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623213-1D92878000000578-351_154x115.jpg" height="115" width="154" alt="Underdog spirit: Atletico Madrid boss Diego Simeone believes fans in Spain want his side to win La Liga" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Simeone reckons La Liga fans want Atletico to beat Barcelona and Real Madrid to the title
            </strong>
            Atletico Madrid's Diego Simeone believes Spain is backing his team
          </span>
        </a>
      </li>
      <li>
        <a href="/sport/football/article-2623090/James-Wilson-insists-come-Manchester-United-scoring-twice-debut-against-Hull.html" class="bottom">
          <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/article-2623090-1DA0288C00000578-410_154x115.jpg" height="115" width="154" alt="History: United have always brought academy players, like Wilson, into their first team" />
          <span class="pufftext">
            <span class="arrow-small-r"></span>
            <strong>
            Wilson insists there is more to come from him after scoring twice on his United debut
            </strong>
            Man United striker James Wilson expects to keep improving
          </span>
        </a>
      </li>
    </ul>
    
  </div>

  </div>
  <script type="text/javascript">
    DM.has('p-1602', 'comScore', {
      mo_mod_id: '1000118',
      mo_mod_pos: 'p-1602'
    });
  </script>

        <div class="home item html_snippet_module">
    <!-- <img src='http://tag.researchnow.com/t/beacon?pr=41&ca=CAMPAIGNNAME&pl=PLACEMENTNAME&cr=CREATIVENAME&si=SITENAME&adn=3&tt=3' /> -->
  </div>

  </div>
  </div>
    <div class="gamma">
        <div class="item video_carousel_module_wrapper">
    <div class="sport  video_carousel_container cleared" id="p-1606"
       data-track-module="sm-722^video_carousel_module"
       data-track-selector=".videoLink"
       data-track-type="cl">
      <div class="video_carousel_title bdrcc">
        <div class="wocc carousel-title">VIDEO</div>
        <img src="http://i.dailymail.co.uk/i/furniture/standard_modules/video/icon_filmstrip.png" />
        <div class="channel-title">WATCH: TODAY'S TOP SPORT VIDEOS</div>
        <div class="rotator-title">
          <ul class="rotator-pages">
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="1"><span class="usability">1</span></a>
            </li>
            <li class="linkro-wocc link-wocc">
              <a href="#" data-page="2"><span class="usability">2</span></a>
            </li>
          </ul>
        </div>
      </div>

      <div class="video-carousel-body">
        <div class="link-wox linkro-ccox left">
          <a class="js-move-prev" href="#">
            <div class="left_scroll"><span></span></div>
          </a>
          <div class="blank-div"></div>
        </div>
        <div class="rotator link-wocc linkro-womlcc">
          <ul class="js-itemList rotator-panels">
            <li class="item">
              <a class="videoLink" href="/video/othersports/video-1093766/TV-sports-hostess-goes-viral-provocative-courtside-display.html"
                data-videoid="3541106232001"
                data-channel="othersports"
                data-source="Other"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093766&amp;colour=sport&amp;item-type=sm&amp;item-id=722 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/06/video-undefined-1D9D831800000578-692_636x362.jpg" alt=""/>
                <div class="video-item-time"><p>26795</p></div>
                <div class="video-item-title bdrcc">TV sports hostess goes viral with provocative courtside display at LA Clippers match</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/football/video-1093865/James-Wilson-scores-past-Newcastle-U18s-match.html"
                data-videoid="3543280689001"
                data-channel="football"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093865&amp;colour=sport&amp;item-type=sm&amp;item-id=722 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA2B24600000578-496_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>81619</p></div>
                <div class="video-item-title bdrcc">James Wilson scores five past Newcastle in U18s match as United win 7-1</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/football/video-1093896/Van-Persie-shows-keepy-uppy-skills-rolled-scarf.html"
                data-videoid="3543214652001"
                data-channel="football"
                data-source="Instagram"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093896&amp;colour=sport&amp;item-type=sm&amp;item-id=722 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA0919600000578-894_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>29049</p></div>
                <div class="video-item-title bdrcc">Robin van Persie shows his keepy uppy skills with rolled up scarf after last home win</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/football/video-1093947/Keeper-sold-dummies-Kyoto-Sanga-score-outrageous-free-kick.html"
                data-videoid="3543392955001"
                data-channel="football"
                data-source="Other"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093947&amp;colour=sport&amp;item-type=sm&amp;item-id=722 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA45B3900000578-756_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>7292</p></div>
                <div class="video-item-title bdrcc">Keeper sold four dummies as Kyoto Sanga score outrageous free-kick</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/boxing/video-1094060/Mayweathers-girls-count-$100000-fastest.html"
                data-videoid="3546072708001"
                data-channel="boxing"
                data-source="Instagram"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1094060&amp;colour=sport&amp;item-type=sm&amp;item-id=722 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/08/video-undefined-1DA9F52500000578-215_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>30094</p></div>
                <div class="video-item-title bdrcc">Mayweather and his girls... who can count to $100,000 the fastest?</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/football/video-1093221/The-worlds-fastest-player-Fanimo-scoring-England-U17s.html"
                data-videoid="3529692501001"
                data-channel="football"
                data-source="FATV"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093221&amp;colour=sport&amp;item-type=sm&amp;item-id=722 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/02/video-undefined-1D83AE4400000578-144_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>202664</p></div>
                <div class="video-item-title bdrcc">The world's fastest player Matthias Fanimo scoring for England U17s</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/football/video-1093864/Gerrard-You-slips-away.html"
                data-videoid="3543214680001"
                data-channel="football"
                data-source="Hayters"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093864&amp;colour=sport&amp;item-type=sm&amp;item-id=722 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/07/video-undefined-1DA25F9000000578-3_636x358.jpg" alt=""/>
                <div class="video-item-time"><p>91952</p></div>
                <div class="video-item-title bdrcc">Gerrard: You never get too down when one slips away, literally slips away</div>
              </a>
            </li>
            <li class="item">
              <a class="videoLink" href="/video/football/video-1093748/Barcelonas-Beckham-Virginia-Torrecilla-scores-half.html"
                data-videoid="3541207768001"
                data-channel="football"
                data-source="YouTube"
                data-modal-type="video-lightbox"
                data-target="/api/video-carousel.html?video-id=1093748&amp;colour=sport&amp;item-type=sm&amp;item-id=722 .video-lightbox">
                <span class="wocc">
                  <div class="playbtn"></div>
                    Watch video
                </span>
                <img src="http://i.dailymail.co.uk/i/pix/2014/05/06/video-undefined-1D9DB66400000578-650_636x362.jpg" alt=""/>
                <div class="video-item-time"><p>25241</p></div>
                <div class="video-item-title bdrcc">Barcelona's Beckham: Virginia Torrecilla scores from her own half</div>
              </a>
            </li>
          </ul>
        </div>
        <div class="link-wox linkro-ccox right">
          <a class="js-move-next" href="#">
            <div class="right_scroll"><span></span></div>
          </a>
          <div class="blank-div"></div>
        </div>
      </div>
  </div>
  <script type="text/javascript">
  DM.has("p-1606", 'videoChannelCarouselModule',
         {"player" : "1989148206001",
          "playerKey" : "AQ~~,AAAAAFSL1bg~,CmS1EFtcMWELN_eSE9A7gpcGWF5XAVmI",
          "nonEmbeddablePlayerIdent" : "2572801325001",
          "nonEmbeddablePlayerKey" : "AQ~~,AAAAAFSL1bg~,CmS1EFtcMWF3nDd2YNUcSIWL0H_o4As-",
          "trackingType" : "carousel_triple",
          "channelShortName" : "sport",
          "overlayType" : "carousel",
          "pageCount" : "2",
          "pageSize" : 3,
          "onPos": 0,
          "updateStyleOnHover": true,
          "videoPlayerConfigMap": {'3541106232001' : 'false','3543280689001' : 'false','3543214652001' : 'false','3543392955001' : 'false','3546072708001' : 'false','3529692501001' : 'false','3543214680001' : 'false','3541207768001' : 'false'},
          "rsi" : typeof(adverts) != 'undefined' && typeof (adverts.getRsiValues) != 'undefined' ? adverts.getRsiValues() : null
  });
  </script>


  </div>

  </div>
    <div class="cleared">
        <div class="alpha">
     
  </div>

        <div class="beta">
        
  </div>
  </div>
    <div class="gamma">
        <div class="home item thin_divide_module">
    <div class="thin-split ccox link-ccox linkro-box bdrcc">
    <h6>
        
    </h6>
  </div>

  </div>

  </div>

    
    
        <script type="text/javascript">
        
        DM.has('content', 'shareLinks', { isChannel: true,
        'anchor': 'tl'});
        </script>
        <script type='text/javascript' src='/dwr/interface/AjaxPoll.js'></script>
        <script type='text/javascript' src='/dwr/interface/AjaxFeedsFacade.js'></script>
        <script type='text/javascript' src='/dwr/interface/AjaxNewsletter.js'></script>
        <script type='text/javascript' src='/dwr/interface/AjaxWeatherHelper.js'></script>
        <script type='text/javascript' src='/dwr/engine.js'></script>
        <script type="text/javascript" src="http://scripts.dailymail.co.uk/static/gunther/gunther-535/dm2--.js" ></script>
        <script type='text/javascript'>
        DM.BC.videoAdServerUrl = "http://pubads.g.doubleclick.net/gampad/ads?sz=8x8&iu=%2F5765%2Fdm.video%2Fdm_video_homehp&ciu_szs=&impl=s&gdfp_req=1&env=vp&output=xml_vast2&unviewed_position_start=1&url=[referrer_url]&correlator=[timestamp]";
        </script>
        
        <script type="text/javascript" >
        
        var GUNTHER = {};
                GUNTHER.bundleLocation = "http://scripts.dailymail.co.uk/static/gunther/";
                GUNTHER.registrationBundleVersion = "gunther-440";
        </script>
        
        <script src="http://admin.brightcove.com/js/BrightcoveExperiences.js" type="text/javascript"></script>
        
        
        
        
        




      <script type="text/javascript" src="http://scripts.dailymail.co.uk/static/bundles/rc-main-140318154402.js"></script>

        
        
        <script type="text/javascript">
        if (typeof DM !== "undefined" && typeof DM.Fn !== "undefined") {
        DM.Fn.init();
        }
        </script>
        
        <!--[if gte IE 8]><!-->
  <script type="text/javascript">
   if (window.FFF === undefined) { window.FFF = {}; }
   window.FFF.env = {"adminHost":"http://and-hsk-femailff-vip.andweb.dmgt.net:8187","imageCropperUrl":"http://mol-hsk-apps-vip.andweb.dmgt.net/imagecropper","name":"production","fffHubHost":"http://www.dailymail.co.uk/femail/fashionfinder","fffPreviewHost":"http://origin-fff.dailymail.co.uk","editorHost":"http://and-hsk-femailff-vip.andweb.dmgt.net","showFFFHubRelatedBanners":true,"fffHost":"http://fff.dailymail.co.uk","googlePlusId":"153480112219.apps.googleusercontent.com","croppedImagesPath":"http://i.dailymail.co.uk/i/fffhub","facebookAppId":146202712090395,"priceGroups":[{"value":"","avg":0,"label":"Choose price range"},{"value":"££££","avg":10000,"label":"500+ (££££)"},{"value":"£££","avg":370,"label":"250-500 (£££)"},{"value":"££","avg":160,"label":"75 - 250 (££)"},{"value":"£","avg":35,"label":"0 - 75 (£)"}],"timeToReEnableSaveButtonsInMilliseconds":10000};
  </script>
  <script type="text/javascript" src="http://scripts.dailymail.co.uk/static/gunther/gunther-535/fff.js" ></script>
  <!--<![endif]-->
        
        <!-- Begin comScore Inline Tag 1.1111.15 -->
        <script type="text/javascript" language="JavaScript1.3" src="http://b.scorecardresearch.com/c2/14366613/cs.js"></script>
        <!-- End comScore Inline Tag -->
        <div class="articleAds articleAds-left" id="js-sky-left">
    <div id="sky-left" class="sky adHolder molads_sky_left_top">
      <script type="text/javascript">
      adverts.addToArray({pos: 'sky_left_top', type: '120x600', target:'COM_SKY_LEFT', wide:true});
      </script>
    </div>
  </div>
        <div class="articleAds articleAds-right" id="js-sky-right">
    <div id="sky-right" class="sky adHolder molads_sky_right_top">
      <script type="text/javascript">
      adverts.addToArray({pos: 'sky_right_top', type:'120x600', target: 'COM_SKY_RIGHT', wide: true});
      </script>
    </div>
    <div class="google-sky">
          <script type="text/javascript" src="http://scripts.dailymail.co.uk/static/gunther/gunther-535/googleads--.js"></script>
      <script type="text/javascript">
        var goog_ad = {};
      </script>

      
      
          <script>
            var google_ad_client = 'ca-an-dailymail';
            goog_ad.prefix = 'uk';
          </script>
        
      

      <script type="text/javascript">
        goog_ad.channel = 'home';
        google_ad_channel = '' + goog_ad.prefix + '_' + goog_ad.channel;
      </script>

      <script type="text/javascript">
        google_ad_output = 'js';
        google_ad_type = 'text';
        google_ad_type_location = 'sky'
        google_language = 'en';
        google_encoding = 'utf8';
        google_safe = 'high';
        google_ad_section = 's1 s2';
        google_feedback = 'on';
        google_max_num_ads = 5;
        google_skip = 4;
      </script>

       <script type="text/javascript">
         adverts.requestGoogleAd(true, 'sky');
       </script>
    </div>
   </div>

        <div class="hiddenAd" id="ad-abs-0-ad">
    <script type="text/javascript">adverts.addToArray({pos: 'mpu_channel', id: 'abs-ad-0', type: '300x250'});</script>
  </div>
  <script type="text/javascript">
    adverts.init();
  </script>
  <script type="text/javascript" src="http://js.revsci.net/gateway/gw.js?csid=D05509&auto=t"></script>
    
        </div>
        <div class="footer" id="footer"
    data-track-module="nav-footer^footer" data-track-selector=".dm-tab-pane a" data-track-pos="static">
    <ul class="home dm-tabs cleared js-links">
      <li class="cnr-5 link-wocc">
        <span class="tl"> </span>
        <span class="tr"> </span>
        <a href="#top">Back to top</a>
      </li>
    </ul>
    <div id="footer-1" class="dm-tab-pane">
      <ul class="nav-primary cleared bdrgr3">
          <li class="home">
    <span class="link-ccox linkro-ccox">
      <a href="/home/index.html" class="no-border">Home</a>
    </span>
  </li>
          <li class="news">
    <span class="link-gr6ox linkro-ccox">
      <a href="/news/index.html" >News</a>
    </span>
  </li>
          <li class="home">
    <span class="link-gr6ox linkro-ccox">
      <a href="/ushome/index.html" >U.S.</a>
    </span>
  </li>
          <li class="sport">
    <span class="link-gr6ox linkro-ccox">
      <a href="/sport/index.html" >Sport</a>
    </span>
  </li>
          <li class="tvshowbiz">
    <span class="link-gr6ox linkro-ccox">
      <a href="/tvshowbiz/index.html" >TV&amp;Showbiz</a>
    </span>
  </li>
          <li class="femail">
    <span class="link-gr6ox linkro-ccox">
      <a href="/femail/index.html" >Femail</a>
    </span>
  </li>
          <li class="health">
    <span class="link-gr6ox linkro-ccox">
      <a href="/health/index.html" >Health</a>
    </span>
  </li>
          <li class="sciencetech">
    <span class="link-gr6ox linkro-ccox">
      <a href="/sciencetech/index.html" >Science</a>
    </span>
  </li>
          <li class="money">
    <span class="link-gr6ox linkro-ccox">
      <a href="/money/index.html" >Money</a>
    </span>
  </li>
          <li class="video">
    <span class="link-gr6ox linkro-ccox">
      <a href="/video/index.html" >Video</a>
    </span>
  </li>
          <li class="coffeebreak">
    <span class="link-gr6ox linkro-ccox">
      <a href="/coffeebreak/index.html" >Coffee Break</a>
    </span>
  </li>
          <li class="travel">
    <span class="link-gr6ox linkro-ccox">
      <a href="/travel/index.html" >Travel</a>
    </span>
  </li>
          <li class="femail">
    <span class="link-gr6ox linkro-ccox">
      <a href="/femail/fashionfinder/index.html" >Fashion Finder</a>
    </span>
  </li>
      </ul>
    </div>
  </div>
  <script type="text/javascript">
     DM.Footer();
  </script>


  <div class="page-footer"
    data-track-module="nav-page_footer^page_footer" data-track-pos="static">
    <a href="/home/sitemap.html" >Sitemap</a>
    <a href="/home/sitemaparchive/index.html" >Archive</a>
    <a href="/mobile">Mobile Apps</a>
    <a href="/home/rssMenu.html" >RSS</a>
    <a href="/textbased/channel-1/index.html" rel="nofollow">Text-based site</a>
    <a href="http://mailpictures.newsprints.co.uk" target="_blank" rel="nofollow" title="Daily Mail Pictures">Reader Prints</a>
    <a href="/ourpapers" target="_blank" rel="nofollow" title="Our Papers">Our Papers</a>
    <a href="#top" class="last" >Top of page</a>
    <br/>
    <a href="http://www.dailymail.co.uk" target="_blank" rel="nofollow" title="News, sport, health and showbiz from The Daily Mail">Daily Mail</a>
    <a href="http://www.mailonsunday.co.uk" target="_blank" rel="nofollow"  title="News, sport and showbiz from The Mail on Sunday">Mail on Sunday</a>
    <a href="http://www.thisisgloucestershire.co.uk/towns.html" target="_blank" rel="nofollow" title="At the heart of all things local">This is Network</a>
    <a href="http://www.thisislondon.co.uk" target="_blank" rel="nofollow" title="Entertainment listings, reviews and showbiz from The Evening Standard">This is London</a>
    <a href="http://www.thisismoney.co.uk" title="Financial Advice, News, Help &amp; Guides from This is Money UK" target="_blank" rel="nofollow" class="last">This is Money</a>
    <br/>
    <a href="http://www.metro.co.uk" target="_blank" rel="nofollow" title="Competitions, games and offbeat stories from Metro">Metro</a>
    <a href="http://www.jobsite.co.uk" target="_blank" rel="nofollow" title="Award-winning UK job search and jobs by email service">Jobsite</a>
    <a href="http://www.mailtravel.co.uk" target="_blank" rel="nofollow" title="Mail Travel">Mail Travel</a>
    <a href="http://www.zoopla.co.uk" target="_blank" rel="nofollow" title="Find your ideal house, flat or apartment for sale or rent">Zoopla.co.uk</a>
    <a href="http://www.primelocation.com" target="_blank" rel="nofollow" title="Search thousands of prime properties for sale or rent">Prime Location</a>
    <a href="http://www.villarenters.com/" target="_blank" rel="nofollow" title="Holiday Rentals" class="last">Villa Holidays</a>
  </div>
  <div class="and-footer"
    data-track-module="nav-and_footer^and_footer" data-track-pos="static">
    <p>Published by Associated Newspapers Ltd</p>
    <p>Part of the Daily Mail, The Mail on Sunday &amp; Metro Media Group</p>

    

    <a href="http://www.and.co.uk/" target="_blank" rel="nofollow" class="copyRight last">&copy; Associated Newspapers Ltd</a>
    <a href="/contactus" >Contact us</a>
    <a rel="nofollow" target="_blank" href="http://www.mailconnected.co.uk/">Advertise with us</a>
    <a href="/terms" >Terms</a>
    <a href="/privacy" >Privacy policy &amp; cookies</a>
    <a href="/additionalcookieinfo" title="Find out more information about cookies on this website" class="cookies last"><img src="http://i.dailymail.co.uk/i/furniture/misc/logo_cookie_reg.png" alt="Cookie regulation logo" width="12" height="12" /></a>
  </div>




    
        <div id="banner" class="banner adHolder">
      <script type="text/javascript">
          adverts.addToArray({type:'468x60', target: 'NON_LEADERBOARD', pos: 'banner_top', dcopt: true});
      </script>
  </div>
    
        </div>
        <div class="banner-adverts">
          <div id="stickyBanner" class="adHolder sticky_banner_overrides">
            <script type="text/javascript">
            adverts.addToArray({type: '980x90', pos: 'sticky_banner', command: "pfadj", adProbe: true, dcopt: true});
            </script>
          </div>
          <div id="superBanner" class="adHolder">
            <script type="text/javascript">
            adverts.addToArray({type: '468x60,728x90,900x125', pos: 'ldr_top', adProbe: true, dcopt: true});
            </script>
          </div>
         </div>    </div>
      <script>
    window._taboola = window._taboola || [];
    _taboola.push({flush:true});
  </script>
      <iframe id="lightbox-shim"></iframe>
      <div id="overlay">&nbsp;</div>
      <div id="lightbox-container" class="cnr8">
          <table id="lightbox" class="ox-iw" summary="lightbox">
              <tr>
                  <td class="tl"></td>
                  <td></td>
                  <td class="tr"></td>
              </tr>
              <tr>
                  <td></td>
                  <td>
                      <div id="lightbox-content">
                          <div id="lightbox-default-container">&nbsp;</div>
                          <div id="lightbox-fader">&nbsp;</div>
                      </div>
                  </td>
                  <td></td>
              </tr>
              <tr>
                  <td class="bl"></td>
                  <td></td>
                  <td class="br"></td>
              </tr>
          </table>
      </div>
    
      
        <script type="text/javascript" src="http://tags.crwdcntrl.net/c/991/cc.js?ns=_cc991" id="LOTCC_991"></script>
        <script type="text/javascript">
        _cc991.bcp();
        </script>
      
    
      
    </body>
  </html>
"""


from collections import defaultdict
import random
import string

import json
from pprint import pprint
json_data=open('mail.json')

input = []

for line in json_data:

    data = json.loads(line)
    sentence = data["headline"]#.decode('unicode_escape').encode('ascii', 'ignore')
    input.append(sentence)

json_data.close()


def generatemk(input):
    mkchain = defaultdict(list)

    for sentence in input:
        sentence = "".join(l for l in sentence if l not in string.punctuation)
        words = sentence.split()

        for word in range(len(words)-1):

            first = words[word].lower().strip()

            second = words[word+1].lower().strip()

            if first.isdigit():
                first = "DIGITT"

            if second.isdigit():
                second = "DIGITT"
            
            mkchain[first].append(second)

    return mkchain

def outsentence(mkchain):
    word = random.choice(mkchain.keys())
    sentence = word

    for idx in range(25):
        try:
            # print word 
            # print mkchain[word] 
            word = random.choice(mkchain[word])

            if word == "DIGITT":
                sentence += " " + str(random.randint(0, 2015))
            else:
                sentence += " " + word

        except IndexError:
            return sentence

    return sentence    


@route('/')
def index():
    a = generatemk(input)
    params = {}
    for i in range(1, 133):
        params['headline%d' % i] = outsentence(a)
    return template(code, **params)

run(host='localhost', port=8080)
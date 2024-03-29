(window.webpackJsonp=window.webpackJsonp||[]).push([[9],{JdaY:function(module,e,t){"use strict";t.r(e);var n,r=t("BJ98"),a=t.n(r),o=t("q1tI"),s=t("pR6o"),i=t("+LJP"),u=t("kwmr"),d=t("sQ/U"),c=t("EdUP"),l=t("TOZ3"),S=t("8WNh"),f=t("b+2U"),h=t("xPfO"),p=t("S+eF"),g=t.n(p),m=t("8c4I"),O=t("DnuM"),v=t("IG+7"),loadCourseDomains=function(e){var t=Object(O.a)("/api/domains.v1",{type:"rest"});return void 0!==e.getStore(v.a).domains?g()():g()(t.get("?fields=id,name")).then((function(t){e.dispatch("LOAD_DOMAINS",t.elements)}))},I=t("tPFS"),E=t("fw5G"),L=t.n(E),D=t("TSOT"),b=Object(D.a)("/api/onDemandHomeProgress.v1",{type:"rest"}),loadCourseHomeProgress=function(e,t){return e.getStore(I.a).hasLoaded()?g()():d.a.isAuthenticatedUser()?function(e){var t="".concat(d.a.get().id,"~").concat(e),n=new L.a(t).addQueryParam("fields","modulesCompleted,modulesPassed");return g()(b.get(n.toString()))}(t).then((function(t){t.elements&&t.elements.length&&e.dispatch("LOAD_HOME_PROGRESS",t.elements[0])})).fail((function(){e.dispatch("LOAD_HOME_PROGRESS",{modulesCompleted:[],modulesPassed:[]})})):(e.dispatch("LOAD_HOME_PROGRESS",{modulesCompleted:[],modulesPassed:[]}),g()())},w=t("hw75"),loadCourseReferences=function(e,t){var n=Object(D.a)("/api/onDemandReferences.v1",{type:"rest"}),r=(new L.a).addQueryParam("courseId",t).addQueryParam("q","courseListed").addQueryParam("fields","name,shortId,slug,content").addQueryParam("includes","assets");return g()(n.get(r.toString())).then((function(t){e.dispatch("LOAD_REFERENCES_LIST",t.elements)}))},A=t("uJqh"),C=Object(D.a)("/api/onDemandCourseSchedules.v1"),courseSchedule=function(e){if(!e)throw new Error("`courseId` is required to get course schedule.");return function(e){var t=new L.a(e).addQueryParam("fields","defaultSchedule");return g()(C.get(t.toString()))}(e).then(A.a).then((function(e){return e.elements[0].defaultSchedule.periods}))},P=t("qgMw"),y=t("lqQ6"),loadCourseSchedule=function(e,t){return e.getStore(P.a).hasLoaded()?g()():t?courseSchedule(t).then((function(t){e.dispatch("LOAD_COURSE_SCHEDULE",t)})):g.a.reject(new y.a("courseId must be provided."))},R=t("fghW"),j=t("++Ya"),k=t("QMiy"),M=t("ihi0"),H=t("IA/e"),U=t("xiyk"),loadS12n=function(e,t){return e.getStore(R.a).hasLoaded()?g()():Object(U.b)(t,d.a.get().id).then((function(e){var t,r,a,o,s,i=(n=e).elements,u=i&&i[0];return u&&d.a.isAuthenticatedUser()?(t=u.id,r=!0,a=d.a.get().id,o=Object(j.c)([a,"Specialization",t]),(s=Object(k.a)(o,{productType:"Specialization"}).then((function(e){var t=e.elements[0],n=t.s12nCourseOwnerships;return r?t=Object.assign({},t,{s12nCourseOwnerships:n||[]}):(t=Object.assign({},t,{s12nCourseOwnerships:new M.a(n||[])}),new H.a(t))})).fail((function(){return r?{id:Object(j.c)([a,t]),userId:a,productId:t,s12nCourseOwnerships:{}}:new H.a({id:Object(j.c)([a,t]),userId:a,productId:t,s12nCourseOwnerships:new M.a})}))).done(),s):g()()})).then((function(t){return e.dispatch("LOAD_S12N",{rawS12ns:n,rawOwnership:t}),{rawS12ns:n,rawOwnership:t}}));var n},ComputedModelActions_loadComputedModels=function(e,t){var n=t.courseSlug,r=t.courseId;return e.getStore(m.a).hasLoaded()?g()():g.a.all([loadCourseDomains(e),loadS12n(e,r),Object(w.a)(e,n),loadCourseSchedule(e,r),loadCourseReferences(e,r),loadCourseHomeProgress(e,r)]).then((function(){e.dispatch("LOAD_COMPUTED_MODELS")}))},T=t("knci"),N=t("15pW"),loadCourseV1=function(e,t){if(e.getStore(v.a).haveCourseIdentifiersLoaded())return g()();if(!t)throw new Error("Missing courseSlug");return function(e){var t=Object(O.a)("/api/courses.v1",{type:"rest"}),n=(new L.a).addQueryParam("q","slug").addQueryParam("slug",e).addQueryParam("fields","certificates,courseTypeMetadata.v1(courseTypeMetadata)").addQueryParam("includes","courseTypeMetadata").addQueryParam("showHidden",!0);return g()(t.get(n.toString())).then((function(t){var n;if("notFound"===t.errorCode)return null;var r=t.elements[0],a=r.id,o=r.certificates,s=null===(n=t.linked["courseTypeMetadata.v1"][0])||void 0===n?void 0:n.courseTypeMetadata;return N.d.courseId=a,N.d.courseSlug=e,{courseId:a,courseCertificates:o,courseTypeMetadata:s}}))}(t).then((function(n){var r=n.courseId,a=n.courseCertificates,o=n.courseTypeMetadata;if(!r)throw new Error("Missing courseId");return e.dispatch("SET_COURSE_IDENTIFIERS",{courseId:r,courseSlug:t,courseCertificates:a,courseTypeMetadata:o}),{courseId:r,courseSlug:t,courseCertificates:a,courseTypeMetadata:o}})).catch((function(n){console.error("Error getting courseId and courseCertificates from courseSlug: ".concat(t,": "),n,n.stack);var r=[];return e.dispatch("SET_COURSE_IDENTIFIERS",{courseId:"",courseSlug:t,courseCertificates:r,courseTypeMetadata:{}}),g()({courseId:"",courseSlug:t,courseCertificates:r})}))},x=t("F/us"),G=t.n(x),Q=t("EGED"),F=t("Eq6n"),q=t("ORjh"),GroupSettingActions_loadUserGroupsForCourse=function(e,t){var n=t.courseId,r=t.userId;return e.getStore("GroupSettingStore").hasLoaded()?g()():q.a.myCourseGroupsWithSettings(r,n).then((function(t){var n=G()(t.linked["groupSettings.v1"]).map((function(e){return new F.a(e)})),r=t.linked["groups.v1"].map((function(e){return new Q.a(e)})),a=t.elements;e.dispatch("LOADED_COURSE_GROUPS",{groups:r,groupSettings:n,groupMemberships:a})})).fail((function(t){e.dispatch("LOADED_COURSE_GROUPS",{})}))},GroupSettingActions_loadUserSessionGroupForCourse=function(e,t){var n=t.courseId,r=t.userId,a=t.sessionId;return e.getStore("GroupSettingStore").hasSessionGroupLoaded()?g()():q.a.getCourseSessionGroup(r,n,a).then((function(t){var n=t.elements[0];e.dispatch("LOADED_SESSION_GROUP",{sessionGroup:n})})).fail((function(t){e.dispatch("LOADED_SESSION_GROUP",{})}))},V=t("3tO9"),J=t.n(V),W=t("8kE/"),z=t("lvha"),B=t("Doqk"),Y=t("QU0K"),memberships_membershipsData=function(e){return Object(z.b)(B.a.build(Y.a.prototype.resourceName,e))},K=Object(W.a)(memberships_membershipsData),X=t("oCg5"),Z=t("7eiT"),ee=t("FOnF"),te={showHidden:!0,fields:["courseId","grade"],includes:{vcMembership:{fields:["certificateCode","grade","grantedAt"]},course:{fields:[]}}},CertificateActions_loadCertificateData=function(e,t){var n,r=t.courseId,a=t.userId;return e.getStore("CertificateStore").hasLoaded()?g()():((n=a?function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};return K(e).then((function(t){if(t.linked&&t.linked["onDemandSessions.v1"]&&t.linked["onDemandSessionMemberships.v1"]){var n=G()(t.linked["onDemandSessions.v1"]).groupBy("courseId"),r=G()(t.linked["onDemandSessionMemberships.v1"]).groupBy("sessionId"),a=Object.keys(r);t.elements.forEach((function(e){var t=n[e.courseId]||[];if(t.length){var o=t.filter((function(e){return a.indexOf(e.id)>=0}));if(o.length){var s=new ee.b(o).getLastSession();e.onDemandSessionId=s.id,e.onDemandSessionMemberships=o.map((function(e){return r[e.id]}))}}}))}if(t.linked&&t.linked["v1Details.v1"]&&(t.linked["courses.v1"]=G()(t.linked["courses.v1"]).map((function(e){if("v1.session"===e.courseType||"v1.capstone"===e.courseType){e.v1Details=e.id;var n=G()(t.linked["v1Sessions.v1"]).reduce((function(t,n){return n.courseId===e.id&&t.push(n.id.toString()),t}),[]);e.v1Sessions=n}return e}))),t.linked&&t.linked["v2Details.v1"]&&(t.linked["courses.v1"]=G()(t.linked["courses.v1"]).map((function(e){return"v2.ondemand"===e.courseType&&(e.v2Details=G()(t.linked["v2Details.v1"]).findWhere({id:e.id})),e}))),t.linked&&t.linked["vcMemberships.v1"]){var o=G()(t.linked["vcMemberships.v1"]).pluck("id");t.elements=G()(t.elements).map((function(e){return G()(o).contains(e.id)&&(e.vcMembershipId=e.id),e}))}if(t.linked&&t.linked["courses.v1"]){var s=G()(t.linked["courses.v1"]).pluck("id");t.elements=G()(t.elements).chain().filter((function(e){return G()(s).contains(e.courseId)})).compact().value()}return t.linked&&t.linked["signatureTrackProfiles.v1"]&&G()(t.elements).each((function(e){e.signatureTrackProfile=e.userId})),e.rawData?t:e.withPaging?{elements:Object(X.a)(Z.a.prototype.resourceName,t),paging:t.paging}:Object(X.a)(Z.a.prototype.resourceName,t)})).fail((function(t){return e.rawData?null:new Z.a}))}(J()(J()({id:"".concat(a,"~").concat(r)},te),{},{rawData:!0})).then((function(t){e.dispatch("LOAD_MEMBERSHIPS",t)})):g()().then((function(){e.dispatch("LOAD_MEMBERSHIPS",null)}))).done(),n)},ne=t("ML/G"),re=t("GnyC"),ae=t("udpv"),oe=Object(D.a)("/api/onDemandDeadlineSettings.v1",{type:"rest"}),se={getStartTime:function(e){var t=(new L.a).addQueryParam("q","byUserAndCourse").addQueryParam("userId",d.a.get().id).addQueryParam("courseId",e).toString();return g()(oe.get(t)).fail((function(e){console.error(e)}))},sendStartTime:function(e,t){var n={data:{userId:d.a.get().id,courseId:t,start:Date.now(),isEnabled:e}};return g()(oe.post("",n))},disableDeadlines:function(e){return se.sendStartTime(!1,e)},getResetPreview:function(e,t){var n=(new L.a).addQueryParam("q","extendPreview").addQueryParam("userId",d.a.get().id).addQueryParam("courseId",e).addQueryParam("extendedAt",Date.now()).toString();g()(oe.get(n)).then(t).fail((function(e){console.error(e)})).done()},resetDeadlines:function(e){var t={data:{userId:d.a.get().id,courseId:e,extendedAt:Date.now()}},n=(new L.a).addQueryParam("action","extend").toString();return g()(oe.post(n,t))}},ie=se,ue=(se.getStartTime,se.sendStartTime,se.disableDeadlines,se.getResetPreview,se.resetDeadlines,function(e,t){var n=t.deadlines,r=n.isEnabled,a=n.moduleDeadlines;r?e.dispatch("LOAD_COURSE_DEADLINES",{moduleDeadlines:a}):e.dispatch("DISABLE_DEADLINES")}),CourseDeadlineActions_enableDeadlines=function(e){var t=e.getStore("CourseStore").getCourseId();return ie.sendStartTime(!0,t).fail((function(e){throw e})).then(A.a).then((function(t){var n=t.elements,r=n[0].start;return ne.a.pushV2(["open_course_home.welcome.emit.course_deadline_set",{first_week_due_time:r}]),e.executeAction(ue,{deadlines:n[0]})}))},CourseDeadlineActions_setDeadlinesIfEligible=function(e){var t=e.getStore("CourseStore"),n=e.getStore("CourseScheduleStore"),r=e.getStore("ProgressStore"),a=Object(re.a)(t,n,r),o=t.getCourseId(),s=e.getStore("CourseMembershipStore").isEnrolled(),i=e.getStore("SessionStore");return Object(ae.a)(o)||i.isSessionsCourse()||1!==a||!s?g()():e.executeAction(CourseDeadlineActions_enableDeadlines,{})},CourseDeadlineActions_loadCourseDeadlines=function(e,t){var n=t.userId,r=e.getStore("CourseStore").getCourseId(),a=e.getStore("CourseMembershipStore").isEnrolled(),o=e.getStore("SessionStore");e.getStore("CourseStore").isReal();if(!a||!n||Object(ae.a)(r))return g()();if(o.isSessionsEnabled()){if(o.isEnrolled()){var s=o.getSession(),i={moduleDeadlines:s.moduleDeadlines};i.itemDeadlines=s.itemDeadlines,e.dispatch("LOAD_COURSE_DEADLINES",i)}return g()()}return ie.getStartTime(r).then(A.a).then((function(t){var n=t.elements[0];return n?e.executeAction(ue,{deadlines:n}):e.executeAction(CourseDeadlineActions_setDeadlinesIfEligible,{})}))},de=t("fHlo"),ce=t("i6HE"),le=t("wJWS"),Se=t("E4RX"),fe=t("5ijc"),he=t("uYOU"),VerificationActions_loadVerificationDisplay=function(e,t){var n=t.authenticated,r=t.userId,a=t.courseId,o=t.s12nId,s=t.isCourseVerificationEnabled;return e.getStore(fe.a).hasLoaded()?g()():n?function(e,t,n,r){if(n&&e){var a=g.a.all([Object(he.a)(e,t,!0)]).spread((function(e){return{isProductVerificationEnabled:n,productOwnership:e,s12nId:r}}),(function(){return null}));return a.done(),a}var o=g()(null);return o.done(),o}(r,a,s,o).then((function(t){e.dispatch("LOAD_VERIFICATION_DISPLAY",t)})):(e.dispatch("LOAD_VERIFICATION_DISPLAY",null),g()())},pe=t("c2GL"),ge=t("sjlm"),me=a()(Object(i.a)((function(e){var t;return{courseSlug:e.params.courseSlug,shouldAllowLabPageAccess:e.location.pathname.endsWith("/lab")&&!(null===(t=e.location.query)||void 0===t||!t.programId)}})),Object(u.a)([h.a,v.a,pe.a,R.a,fe.a,ge.a,m.a,I.a],(function(e,t,n,r,a,o,s,i){return{s12n:r.getS12n(),course:t.getMetadata(),courseId:t.getCourseId(),isEnrolled:n.isEnrolled(),sessionId:e.getSessionId(),isEnrolledInSession:e.isEnrolled(),s12nStoreHasLoaded:r.hasLoaded(),courseStoreHasLoaded:t.hasLoaded(),sessionStoreHasLoaded:e.hasLoaded(),verificationStoreHasLoaded:a.hasLoaded(),courseMembershipStoreHasLoaded:n.hasLoaded(),computedModelStoreHasLoaded:s.hasLoaded(),courseIdentifiersHaveLoaded:t.haveCourseIdentifiersLoaded(),courseViewGradeStoreHasLoaded:o.hasLoaded(),progressStoreHasLoaded:i.hasLoaded()}})),Object(s.a)((function(e,t){var n=t.courseSlug;e.executeAction(loadCourseV1,n)})),Object(c.a)((function(e){return e.courseIdentifiersHaveLoaded})),Object(c.a)((function(e){return!!e.courseId}),o.createElement(T.a,null)),Object(s.a)((function(e,t){var n=t.courseId;e.executeAction(de.a,n)})),Object(c.a)((function(e){return e.courseMembershipStoreHasLoaded})),Object(c.a)((function(e){var t=e.isEnrolled,n=e.shouldAllowLabPageAccess;return d.a.isSuperuser()||t||n}),o.createElement(T.a,null)),Object(s.a)((function(e,t){var n=t.courseSlug,r=t.courseId;e.executeAction(ComputedModelActions_loadComputedModels,{courseSlug:n,courseId:r})})),Object(c.a)((function(e){return e.computedModelStoreHasLoaded})),Object(s.a)((function(e,t){var n=t.courseId,r=t.courseSlug,a=d.a.get().id,o=d.a.isAuthenticatedUser();e.executeAction(f.a,{courseSlug:r}),e.executeAction(ce.a,{courseId:n}),e.executeAction(GroupSettingActions_loadUserGroupsForCourse,{courseId:n,userId:a}),e.executeAction(le.a,{authenticated:o}),e.executeAction(CertificateActions_loadCertificateData,{courseId:n,userId:a}),e.executeAction(Se.a,{authenticated:o,courseId:n,userId:a})})),Object(c.a)((function(e){var t=e.s12nStoreHasLoaded,n=e.courseStoreHasLoaded,r=e.sessionStoreHasLoaded,a=e.courseViewGradeStoreHasLoaded,o=e.progressStoreHasLoaded;return t&&n&&r&&a&&o})),Object(s.a)((function(e,t){var n=t.courseId,r=t.course,a=t.s12n,o=t.sessionId,s=d.a.get().id,i=d.a.isAuthenticatedUser(),u=a&&a.getId(),c=r.isVerificationEnabled();e.getStore("CourseStore");e.executeAction(CourseDeadlineActions_loadCourseDeadlines,{userId:s}),e.executeAction(VerificationActions_loadVerificationDisplay,{authenticated:i,userId:s,courseId:n,isCourseVerificationEnabled:c,s12nId:u}),e.executeAction(GroupSettingActions_loadUserSessionGroupForCourse,{courseId:n,userId:s,sessionId:o})})),Object(c.a)((function(e){return e.verificationStoreHasLoaded})))((function(e){var t=e.children;return t?o.cloneElement(t,{}):null}));e.default=a()(Object(u.a)([fe.a],(function(e){return{isLegacyDataLoaded:e.hasLoaded()}})))((function(e){var t=e.children,r=e.isLegacyDataLoaded;return(o.createElement("div",{className:"rc-LegacyDataFetch"},o.createElement(me,null,t),!r&&(n||(n=o.createElement(l.a,{height:512},o.createElement(S.a,null))))))}))},"b+2U":function(module,e,t){"use strict";t.d(e,"a",(function(){return getCurrentSession})),t.d(e,"b",(function(){return updateEnrollableAndFollowingSessions}));var n=t("S+eF"),r=t.n(n),a=t("xPfO"),o=t("jihO"),getCurrentSession=function(e,t){var n=t.courseSlug;return e.getStore(a.a).hasLoaded()?r()():o.c(n).then((function(t){e.dispatch("LOAD_SESSION",t||null)})).fail((function(e){throw e}))},updateEnrollableAndFollowingSessions=function(e,t){var n=t.courseId,s=t.currentSessionId;return e.getStore(a.a).hasLoaded()?r()():o.d(n,s).then((function(t){(t.getUpcomingSession()||t.getFollowingSession())&&e.dispatch("LOAD_UPCOMING_AND_FOLLOWING_SESSIONS",{upcomingSession:t.getUpcomingSession(),followingSession:t.getFollowingSession()})})).fail((function(e){throw e}))}},knci:function(module,e,t){"use strict";var n,r=t("VbXa"),a=t.n(r),o=t("q1tI"),s=t("+LJP"),i=t("juwT"),u=t("lngd"),d=function(e){function CourseUnauthorized(){return e.apply(this,arguments)||this}a()(CourseUnauthorized,e);var t=CourseUnauthorized.prototype;return t.componentDidMount=function(){var e=this.props.courseSlug;i.a.setLocation("/learn/".concat(e))},t.render=function(){return n||(n=o.createElement("div",{className:"align-horizontal-center"},o.createElement(u.a,null)))},CourseUnauthorized}(o.Component);e.a=Object(s.a)((function(e,t){return{courseSlug:e.params.courseSlug}}))(d)},udpv:function(module,e,t){"use strict";var n=t("/RAd");e.a=function(e){return-1!==n.a.get("defaultDeadlines").indexOf(e)}},wJWS:function(module,e,t){"use strict";t.d(e,"a",(function(){return loadHonorsUserPreferences})),t.d(e,"b",(function(){return setHonorsUserPreferences})),t.d(e,"c",(function(){return setLessonSkipped}));var n=t("S+eF"),r=t.n(n),a=t("tdcm"),loadHonorsUserPreferences=function(e,t){var n=t.authenticated;return e.getStore("HonorsUserPreferencesStore").hasLoaded()?r()():n?a.a.get(a.a.keyEnum.HONORS).then((function(t){e.dispatch("LOAD_HONORS_USER_PREFERENCES",t)})).fail((function(t){e.dispatch("LOAD_HONORS_USER_PREFERENCES",{})})):(e.dispatch("LOAD_HONORS_USER_PREFERENCES",{}),r()())},setHonorsUserPreferences=function(e,t){var n=t.authenticated,o=t.updatedHonorsUserPreferences;return n?a.a.set(a.a.keyEnum.HONORS,o).then((function(){e.dispatch("LOAD_HONORS_USER_PREFERENCES",o)})):(e.dispatch("LOAD_HONORS_USER_PREFERENCES",o),r()())},setLessonSkipped=function(e,t){var n=t.lessonId,r=t.skipped;e.dispatch("SET_LESSON_SKIPPED",{lessonId:n,skipped:r})}}}]);
//# sourceMappingURL=9.796ab632124fb97e0a8e.js.map
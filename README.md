## Custom tools for LLM

This repo aims to build some custom tools fopr LLM applications. For now I'm using for myself with N8N.

The goal is create simple API's to solve simple problems.

 - `GET /convert-url-to-markdown?url={URL_TO_FETCH_CONTENT}` -> Given a url, fetch the html, convert to markdown.

 Looks simple, but I had issues to fetch sites secured by cloudfare. This works, for now... 

### Exemple

URL: https://gurselgazii.medium.com/enhancing-spring-boot-rest-apis-with-threadlocal-6c13eb63da8c

Response:

```markdown
[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6c13eb63da8c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&source=---top_nav_layout_nav----------------------------------)Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fgurselgazii.medium.com%2Fenhancing-spring-boot-rest-apis-with-threadlocal-6c13eb63da8c&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)
[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fgurselgazii.medium.com%2Fenhancing-spring-boot-rest-apis-with-threadlocal-6c13eb63da8c&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)
![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)Enhancing Spring Boot REST APIs with ThreadLocal
================================================
[![Gürsel Gazi İçtüzer](https://miro.medium.com/v2/resize:fill:88:88/1*Vg0gNsFzrjM5ElBt0XnS5A.jpeg)](/?source=post_page---byline--6c13eb63da8c--------------------------------)[Gürsel Gazi İçtüzer](/?source=post_page---byline--6c13eb63da8c--------------------------------)
·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fcb2a15ffc425&operation=register&redirect=https%3A%2F%2Fgurselgazii.medium.com%2Fenhancing-spring-boot-rest-apis-with-threadlocal-6c13eb63da8c&user=G%C3%BCrsel+Gazi+%C4%B0%C3%A7t%C3%BCzer&userId=cb2a15ffc425&source=post_page-cb2a15ffc425--byline--6c13eb63da8c---------------------post_header-----------)
3 min read·Mar 10, 2024
1
Listen
Share
In the modern era of web development, creating efficient, scalable, and maintainable web services is crucial. Spring Boot, a popular framework in the Java ecosystem, simplifies this process, especially when building RESTful APIs. However, managing contextual information across different layers of an application, such as userspecific data or request details, can be challenging. This is where `ThreadLocal` comes into play, offering a way to maintain data that is local to the current thread of execution. In this article, we'll explore how to effectively use `ThreadLocal` in Spring Boot REST APIs.
![]()Understanding ThreadLocal
=========================
`ThreadLocal` in Java provides a way to maintain variables that are accessible only to the current thread. Unlike normal variable storage, where variables are shared among threads, `ThreadLocal` variables are unique to each thread and are not shared. This feature makes `ThreadLocal` particularly useful for managing contextspecific data throughout a request's lifecycle in a web application.
Why Use ThreadLocal in Spring Boot REST APIs?
=============================================
In a Spring Boot REST API, each HTTP request is handled by a separate thread. Sometimes, there is a need to pass userspecific data or request metadata across different layers of the application (e.g., from controllers to services and repositories) without cluttering the method signatures. `ThreadLocal` can help by storing data specific to the current request thread, ensuring that data remains consistent and isolated throughout the execution of the request.
Implementing ThreadLocal in Spring Boot
=======================================
Here’s how you can implement `ThreadLocal` in a Spring Boot application to enhance your REST APIs:
Step 1: Define a ThreadLocal Wrapper
====================================
First, create a wrapper class around `ThreadLocal` that will hold the contextspecific information. For example, if you want to store the current user's information, you can create a class like this:
```
public class UserContext { 
 private static final ThreadLocal<String> currentUser = new ThreadLocal<>(); 
 
 public static String getCurrentUser() { 
 return currentUser.get(); 
 } 
 
 public static void setCurrentUser(String user) { 
 currentUser.set(user); 
 } 
 
 public static void clear() { 
 currentUser.remove(); 
 } 
}
```
Step 2: Set Context Information in Spring Boot Interceptors
===========================================================
Interceptors in Spring Boot can intercept incoming requests and outgoing responses. You can use an interceptor to set the ThreadLocal context at the beginning of a request. For example, you could extract user information from the request header and set it in `UserContext`:
```
@Component 
public class UserInterceptor implements HandlerInterceptor { 
 
 @Override 
 public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception { 
 // Extract user info from the request 
 String user = request.getHeader("User"); 
 // Set the user in the context 
 UserContext.setCurrentUser(user); 
 return true; 
 } 
 
 @Override 
 public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception { 
 // Clear the context once the request is complete 
 UserContext.clear(); 
 } 
}
```
Step 3: Register the Interceptor
================================
Once you have the interceptor, you need to register it with Spring MVC. You can do this by creating a configuration class that implements `WebMvcConfigurer`:
```
@Configuration 
public class WebConfig implements WebMvcConfigurer { 
 
 @Autowired 
 private UserInterceptor userInterceptor; 
 
 @Override 
 public void addInterceptors(InterceptorRegistry registry) { 
 registry.addInterceptor(userInterceptor); 
 } 
}
```
Step 4: Utilize the ThreadLocal Context
=======================================
Now, anywhere in your application, you can access the userspecific data stored in `UserContext` without needing to pass the user information down through every layer:
```
public class SomeService { 
 public void performAction() { 
 String currentUser = UserContext.getCurrentUser(); 
 // Use the currentUser for something specific 
 } 
}
```
Best Practices and Considerations
=================================
* **Memory Leaks**: Always ensure that the data stored in `ThreadLocal` is removed after use, especially in web applications. Failing to clear the `ThreadLocal` can lead to memory leaks.
* **Context Propagation**: Be aware that `ThreadLocal` does not automatically propagate context across different threads, such as in the case of asynchronous processing or when using `@Async`. You may need additional configurations or a different approach for these scenarios.
* **Testing**: Ensure your application is correctly scoped for testing environments, as the same thread may be reused across tests.
Conclusion
==========
Using `ThreadLocal` with Spring Boot REST APIs offers a powerful way to maintain and manage requestspecific data throughout the lifecycle of a request. It enhances the modularity and cleanliness of your code by avoiding the need to pass context data through every layer of your application. By following the steps outlined above and adhering to best practices, you can implement `ThreadLocal` effectively in your Spring Boot applications, resulting in more maintainable and scalable web services.
[Spring Boot](https://medium.com/tag/spring-boot?source=post_page-----6c13eb63da8c--------------------------------)[Rest Api](https://medium.com/tag/rest-api?source=post_page-----6c13eb63da8c--------------------------------)[Threadlocal](https://medium.com/tag/threadlocal?source=post_page-----6c13eb63da8c--------------------------------)

1
[![Gürsel Gazi İçtüzer](https://miro.medium.com/v2/resize:fill:144:144/1*Vg0gNsFzrjM5ElBt0XnS5A.jpeg)](/?source=post_page---post_author_info--6c13eb63da8c--------------------------------)Follow[Written by Gürsel Gazi İçtüzer
------------------------------](/?source=post_page---post_author_info--6c13eb63da8c--------------------------------)[76 Followers](/followers?source=post_page---post_author_info--6c13eb63da8c--------------------------------)Senior Software Developer
Follow[Help](https://help.medium.com/hc/en-us?source=post_page-----6c13eb63da8c--------------------------------)[Status](https://medium.statuspage.io/?source=post_page-----6c13eb63da8c--------------------------------)[About](https://medium.com/about?autoplay=1&source=post_page-----6c13eb63da8c--------------------------------)[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6c13eb63da8c--------------------------------)[Press](pressinquiries@medium.com?source=post_page-----6c13eb63da8c--------------------------------)[Blog](https://blog.medium.com/?source=post_page-----6c13eb63da8c--------------------------------)[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6c13eb63da8c--------------------------------)[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6c13eb63da8c--------------------------------)[Text to speech](https://speechify.com/medium?source=post_page-----6c13eb63da8c--------------------------------)[Teams](https://medium.com/business?source=post_page-----6c13eb63da8c--------------------------------)
```
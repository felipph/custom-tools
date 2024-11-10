





[![The Baeldung logo](https://www.baeldung.com/wp-content/themes/baeldung/icon/logo.svg)](/ "Baeldung")





* * [![The Baeldung Logo](https://www.baeldung.com/wp-content/themes/baeldung/icon/logo.svg)](/ "Baeldung")* [Start Here](/start-here)* [Courses&nbsp;▼▲](javascript:void(0))


	+ [### REST with Spring Boot
	
	
	
	 The canonical reference for building a production grade API with Spring](/courses/rest-with-spring-boot-course "The “REST With Spring” Course")
	+ [### Learn Spring Security&nbsp;▼▲
	
	
	
	 THE unique Spring Security education if you’re working with Java today](/courses/learn-spring-security-course)
	
	
		- [### Learn Spring Security Core
		
		
		
		 Focus on the Core of Spring Security 6](/courses/learn-spring-security-core-course)
		- [### Learn Spring Security OAuth
		
		
		
		 Focus on the new OAuth2 stack in Spring Security 6](/courses/learn-spring-security-oauth-course)
	+ [### Learn Spring
	
	
	
	 From no experience to actually building stuff​](/courses/learn-spring-course)
	+ [### Learn Spring Data JPA
	
	
	
	 The full guide to persistence with Spring Data JPA](/courses/learn-spring-data-jpa-course)* [Guides&nbsp;▼▲](javascript:void(0))


	+ [### Spring Boot
	
	
	
	 Get started and go deep into Spring Boot 3](/spring-boot)
	+ [### Persistence
	
	
	
	 The Persistence with Spring guides](/persistence-with-spring-series)
	+ [### REST
	
	
	
	 The guides on building REST APIs with Spring](/rest-with-spring-series)
	+ [### Security
	
	
	
	 The Spring Security guides](/security-spring)* [About&nbsp;▼▲](javascript:void(0))


	+ [### Full Archive
	
	
	
	 The high level overview of all the articles on the site.](/full_archive)
	+ [### Baeldung Ebooks
	
	
	
	 Discover all of our eBooks](/library/)
	+ [### About Baeldung
	
	
	
	 About Baeldung.](/about)* * [xml version\="1\.0" encoding\="utf\-8"?](/members/ "Pro")*

















Guide to DeferredResult in Spring
=================================















Last updated: March 17, 2024




![](https://secure.gravatar.com/avatar/dc417739e22ae675b0e1f7012bbddaa5?s=50&amp;r=g)

 Written by: 

[baeldung](https://www.baeldung.com/author/baeldung "Posts by baeldung") 




![]()![](https://www.baeldung.com/wp-content/uploads/custom_avatars/T3QS5E410-U8BFPSFCP-47abc3109ab8-512-150x150.png)

 Reviewed by: 

Loredana Crusoveanu

















* [Spring MVC](https://www.baeldung.com/category/spring/spring-web/spring-mvc)







 

Partner – MongoDB – NPI EA (cat\= Artificial Intelligence)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
**Retrieval\-Augmented Generation (RAG)** is a powerful
approach in Artificial Intelligence that's very useful in a variety
of tasks like Q\&amp;A systems, customer support, market research,
personalized recommendations, and more.


A key component of RAG applications is the **vector
database**, which helps manage and retrieve data based on
semantic meaning and context.


Learn how to build a gen AI RAG application with **Spring AI
and the MongoDB vector database** through a practical
example:


**[\&gt;\&gt;
Building a RAG App Using MongoDB and Spring AI](/MongoDB-NPI-EA-gF7Bf)**



Partner – Mockito – NPI EA (tag \= Mockito)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Mocking is an essential part of unit testing, and the Mockito
library makes it easy to write **clean and intuitive unit
tests** for your Java code.


Get started with mocking and improve your application tests
using our **Mockito guide**:


[Download the
eBook](/ebook-mockito-NPI-EA-patak0)



Baeldung Pro – NPI EA (cat \= Baeldung)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Baeldung Pro comes with both absolutely **No\-Ads** as well as
finally with **Dark Mode**, for a clean learning experience:


[\&gt;\&gt; Explore a clean
Baeldung](/baeldung-pro-NPI-EA-tenku)


Once the early\-adopter seats are all used, **the price will go
up and stay at $33/year.**



Partner – Microsoft – NPI EA (cat \= Baeldung)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Azure Container Apps is a fully managed serverless container
service that enables you to **build and deploy modern,
cloud\-native Java applications and microservices** at scale. It
offers a simplified developer experience while providing the
flexibility and portability of containers.


Of course, Azure Container Apps has really solid support for our
ecosystem, from a number of build options, managed Java components,
native metrics, dynamic logger, and quite a bit more.


To learn more about Java features on Azure Container Apps, visit
the [documentation
page](/microsoft-NPI-EA-ejfj2).


You can also ask questions and leave feedback on the Azure
Container Apps [GitHub page](/microsoft-NPI-EA-dsak1).



Partner – Orkes – NPI EA (tag\=Microservices)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Modern software architecture is often broken. Slow delivery
leads to missed opportunities, innovation is stalled due to
architectural complexities, and engineering resources are
exceedingly expensive.


**Orkes is the leading workflow orchestration platform**
built to enable teams to transform the way they develop, connect,
and deploy applications, microservices, AI agents, and more.


With Orkes Conductor managed through Orkes Cloud, developers can
focus on building mission critical applications without worrying
about infrastructure maintenance to meet goals and, simply put,
taking new products live faster and reducing total cost of
ownership.


**Try a [14\-Day
Free Trial of Orkes](/orkes-NPI-EA-DZ5l9) Conductor today.**



Partner – Microsoft – NPI EA (cat\= Spring Boot)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Azure Container Apps is a fully managed serverless container
service that enables you to **build and deploy modern,
cloud\-native Java applications and microservices** at scale. It
offers a simplified developer experience while providing the
flexibility and portability of containers.


Of course, Azure Container Apps has really solid support for our
ecosystem, from a number of build options, managed Java components,
native metrics, dynamic logger, and quite a bit more.


To learn more about Java features on Azure Container Apps, you
can get started over on the [documentation page](/Microsoft-NPI-EA-Frm96).


And, you can also ask questions and leave feedback on the Azure
Container Apps [GitHub page](/microsoft-NPI-EA-su92kh).



Partner – Jmix\-Haulmont – NPI EA (cat\= Spring Boot)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Whether you're just starting out or have years of experience,
**Spring Boot** is obviously a great choice for building a web
application.


Jmix builds on this highly powerful and mature Boot stack,
allowing devs to build and deliver **full\-stack web
applications** without having to code the frontend. Quite
flexibly as well, from simple web GUI CRUD applications to complex
enterprise solutions.


Concretely, **The Jmix Platform** includes a framework built
on top of **Spring Boot, JPA, and Vaadin**, and comes with Jmix
Studio, **an IntelliJ IDEA plugin** equipped with a suite of
developer productivity tools.


The platform comes with interconnected **out\-of\-the\-box
add\-ons** for report generation, BPM, maps, instant web app
generation from a DB, and quite a bit more:


**[\&gt;\&gt; Become an efficient
full\-stack developer with Jmix](/Jmix-Haulmont-NPI-EA-Jki9c)**



Partner – Codium – NPI EA (cat \= Testing)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Get non\-trivial analysis (and trivial, too!) **suggested right
inside your IDE or Git platform** so you can code smart, create
more value, and stay confident when you push.


Get CodiumAI **for free** and become part of a community of
over 280,000 developers who are already experiencing improved and
quicker coding.


Write code that works the way you meant it to:


**[\&gt;\&gt;
CodiumAI. Meaningful Code Tests for Busy Devs](/codium-NPI-EA-tRyN4)**



Partner – Machinet – NPI EA (cat \= Testing)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
The AI Assistant to boost Boost your productivity writing unit
tests \- **Machinet AI**.


AI is all the rage these days, but for very good reason. The
highly practical coding companion, you'll get the power of
AI\-assisted coding and **automated unit test generation**.  

Machinet's **Unit Test AI Agent** utilizes your own project
context to create meaningful unit tests that intelligently aligns
with the behavior of the code.  

And, the **AI Chat** crafts code and fixes errors with ease,
like a helpful sidekick.  



Simplify Your Coding Journey with **Machinet AI**:


**[\&gt;\&gt;
Install Machinet AI in your IntelliJ](/Machinet-NPI-EA-tUt4l)**



eBook – Java Concurrency – NPI EA (cat\=Java Concurrency)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Handling concurrency in an application can be a tricky process
with many **potential pitfalls**. A solid grasp of the
fundamentals will go a long way to help minimize these issues.


Get started with understanding multi\-threaded applications with
our **Java Concurrency** guide:


[\&gt;\&gt; Download
the eBook](/ebook-java-concurrency-NPI-EA-1dad2)



eBook – Reactive – NPI EA (cat\=Reactive)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Spring 5 added support for reactive programming with the Spring
WebFlux module, which has been improved upon ever since. Get
started with the Reactor project basics and **reactive programming
in Spring** Boot:


[\&gt;\&gt; Download the
E\-book](/ebook-reactive-NPI-EA-99iIl)



eBook – Guide Spring Cloud – NPI EA (cat\=Spring Cloud)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Let's get started with a Microservice Architecture with Spring
Cloud:


[Download the Guide](/ebook-guide-spring-cloud-NPI-EA-5iLbb)



eBook – Java Streams – NPI EA (cat\=Java Streams)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Since its introduction in Java 8, the Stream API has become a
staple of Java development. The basic operations like iterating,
filtering, mapping sequences of elements are deceptively simple to
use.


But these can also be overused and fall into some common
pitfalls.


To **get a better understanding on how Streams work** and how
to combine them with other language features, check out our guide
to Java Streams:


[Download the
E\-book](/eBook-Java-Streams-NPI-EA-2!hG6)



eBook – Jackson – NPI EA (cat\=Jackson)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Do JSON right with Jackson


[Download the
E\-book](/ebook-jackson-NPI-EA-5tSar)



eBook – HTTP Client – NPI EA (cat\=Http Client\-Side)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Get the most out of the Apache HTTP Client


[Download the
E\-book](/ebook-http-client-NPI-EA-4WaR3)



eBook – Maven – NPI EA (cat \= Maven)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Get Started with Apache Maven:


[Download the E\-book](/ebook-maven-NPI-EA-k5T!3)



eBook – Persistence – NPI EA (cat\=Persistence)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Working on getting your persistence layer right with Spring?


[Explore the
eBook](/ebook-persistence-NPI-EA-b1Gby)



eBook – RwS – NPI EA (cat\=Spring MVC)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Building a REST API with Spring?


[Download the E\-book](/ebook-rws-NPI-EA-t5m!Y)



Course – LS – NPI EA (cat\=Jackson)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Get started with Spring and Spring Boot, through the *Learn
Spring* course:


**[\&gt;\&gt; LEARN
SPRING](/course-ls-NPI-EA-H9fv8)**
Course – RWSB – NPI EA (cat\=REST)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Explore Spring Boot 3 and Spring 6 in\-depth through building a
full *REST API* with the framework:


**[\&gt;\&gt;
The New “REST With Spring Boot”](/course-rws-npi-ea-h4V3y)**



Course – LS – NPI EA (cat\=Spring)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Get started with Spring and Spring Boot, through the reference
*Learn Spring* course:


**[\&gt;\&gt; LEARN
SPRING](/course-ls-npi-ea-b3tTr)**



Course – LSS – NPI EA (cat\=Spring Security)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Yes, Spring Security can be complex, from the more advanced
functionality within the Core to the deep OAuth support in the
framework.


I built the security material as **two full courses \- Core and
OAuth**, to get practical with these more complex scenarios. We
explore when and how to use each feature and **code through it on
the backing project**.


You can explore the course here:


**[\&gt;\&gt; Learn Spring
Security](/course-lss-NPI-EA-4lL4i)**



Course – LSD – NPI EA (tag\=Spring Data JPA)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Spring Data JPA is a great way to handle the **complexity of
JPA with the powerful simplicity of Spring Boot**.


Get started with Spring Data JPA through the guided reference
course:


**[\&gt;\&gt; CHECK OUT THE
COURSE](/courselsd-NPI-EA-1fOru)**



eBook – RWS – NPI (cat\= Spring MVC)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Building a REST API with Spring 5?


[Download the
E\-book](/eBook-RwS-NPI-vH5Ok)



 




**1\. Overview**
----------------



In this tutorial, we’ll look at **how we can use the&nbsp;*DeferredResult*&nbsp;class in Spring MVC to perform asynchronous request processing**.


Asynchronous support was introduced in Servlet 3\.0 and, simply put, it allows processing an HTTP request in another thread than the request receiver thread.


*DeferredResult,* available from Spring 3\.2 onwards, assists in offloading a long\-running computation from an http\-worker thread to a separate thread.


Although the other thread will take some resources for computation, the worker threads are not blocked in the meantime and can handle incoming client requests.


The async request processing model is very useful as it helps scale an application well during high loads, especially for IO intensive operations.






**2\. Setup**
-------------



For our examples, we’ll use a Spring Boot application. For more details on how to bootstrap the application, refer to our previous&nbsp;[article](/spring-boot-start).


Next, we’ll demonstrate both synchronous and asynchronous communication using *DeferredResult*and also compare how asynchronous one scales better for high load and IO intensive use cases.


**3\. Blocking REST Service**
-----------------------------



Let’s start with developing a standard blocking REST service:



```
@GetMapping("/process-blocking")
public ResponseEntity&lt;?&gt; handleReqSync(Model model) { 
 // ...
 return ResponseEntity.ok("ok");
}
```

The problem here is that **the request processing thread is blocked until the complete request is processed** and the result is returned. In case of long\-running computations, this is a sub\-optimal solution.


To address this, we can make better use of container threads to handle client requests as we’ll see in the next section.






**4\. Non\-Blocking REST Using *DeferredResult***
-------------------------------------------------



To avoid blocking, we’ll use callbacks\-based programming model where instead of the actual result, we’ll return a&nbsp;*DeferredResult* to the servlet container.



```
@GetMapping("/async-deferredresult")
public DeferredResult&lt;ResponseEntity&lt;?&gt;&gt; handleReqDefResult(Model model) {
 LOG.info("Received async-deferredresult request");
 DeferredResult&lt;ResponseEntity&lt;?&gt;&gt; output = new DeferredResult&lt;&gt;();
 
 ForkJoinPool.commonPool().submit(() -&gt; {
 LOG.info("Processing in separate thread");
 try {
 Thread.sleep(6000);
 } catch (InterruptedException e) {
 }
 output.setResult(ResponseEntity.ok("ok"));
 });
 
 LOG.info("servlet thread freed");
 return output;
}
```

**Request processing is done in a separate thread and once completed we invoke the *setResult* operation on the *DeferredResult* object.**


Let’s look at the log output to check that our threads behave as expected:



```
[nio-8080-exec-6] com.baeldung.controller.AsyncDeferredResultController: 
Received async-deferredresult request
[nio-8080-exec-6] com.baeldung.controller.AsyncDeferredResultController: 
Servlet thread freed
[nio-8080-exec-6] java.lang.Thread : Processing in separate thread
```

Internally, the container thread is notified and the HTTP response is delivered to the client. The connection will remain open by the container(servlet 3\.0 or later) until the response arrives or times out.


**5\. *DeferredResult* Callbacks**
----------------------------------



**We can register 3 types of callbacks with a DeferredResult: completion, timeout and error callbacks.**





Let’s use the *onCompletion()* method to define a block of code that’s executed when an async request completes:



```
deferredResult.onCompletion(() -&gt; LOG.info("Processing complete"));
```

Similarly, we can use *onTimeout()* to register custom code to invoke once timeout occurs. In order to limit request processing time, we can pass a timeout value during the&nbsp;*DeferredResult* object creation:



```
DeferredResult&lt;ResponseEntity&lt;?&gt;&gt; deferredResult = new DeferredResult&lt;&gt;(500l);

deferredResult.onTimeout(() -&gt; 
 deferredResult.setErrorResult(
 ResponseEntity.status(HttpStatus.REQUEST_TIMEOUT)
 .body("Request timeout occurred.")));
```

In case of timeouts, we’re setting a different response status via timeout handler registered with *DeferredResult*.


Let’s trigger a timeout error by processing a request that takes more than the defined timeout values of 5 seconds:



```
ForkJoinPool.commonPool().submit(() -&gt; {
 LOG.info("Processing in separate thread");
 try {
 Thread.sleep(6000);
 } catch (InterruptedException e) {
 ...
 }
 deferredResult.setResult(ResponseEntity.ok("OK")));
});
```

Let’s look at the logs:



```
[nio-8080-exec-6] com.baeldung.controller.DeferredResultController: 
servlet thread freed
[nio-8080-exec-6] java.lang.Thread: Processing in separate thread
[nio-8080-exec-6] com.baeldung.controller.DeferredResultController: 
Request timeout occurred
```

There will be scenarios where long\-running computation fails due to some error or exception. In this case, we can also register an *onError()* callback:



```
deferredResult.onError((Throwable t) -&gt; {
 deferredResult.setErrorResult(
 ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
 .body("An error occurred."));
});
```

In case of an error, while computing the response, we’re setting a different response status and message body via this error handler.


**6\. Conclusion**
------------------



In this quick article, we looked at how Spring MVC *DeferredResult* eases the creation of asynchronous endpoints.





As usual, the complete source code is available [over on Github](https://github.com/eugenp/tutorials/tree/master/spring-web-modules/spring-rest-http).


 
 

Partner – Orkes – NPI EA (cat \= Spring)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
Modern software architecture is often broken. Slow delivery
leads to missed opportunities, innovation is stalled due to
architectural complexities, and engineering resources are
exceedingly expensive.


**Orkes is the leading workflow orchestration platform**
built to enable teams to transform the way they develop, connect,
and deploy applications, microservices, AI agents, and more.


With Orkes Conductor managed through Orkes Cloud, developers can
focus on building mission critical applications without worrying
about infrastructure maintenance to meet goals and, simply put,
taking new products live faster and reducing total cost of
ownership.


**Try a [14\-Day
Free Trial of Orkes](/orkes-NPI-EA-B4hH8) Conductor today.**



Partner – Jmix\-Haulmont – NPI EA (cat\= Spring Boot)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

Whether you're just starting out or have years of experience,
**Spring Boot** is obviously a great choice for building a web
application.


Jmix builds on this highly powerful and mature Boot stack,
allowing devs to build and deliver **full\-stack web
applications** without having to code the frontend. Quite
flexibly as well, from simple web GUI CRUD applications to complex
enterprise solutions.


Concretely, **The Jmix Platform** includes a framework built
on top of **Spring Boot, JPA, and Vaadin**, and comes with Jmix
Studio, **an IntelliJ IDEA plugin** equipped with a suite of
developer productivity tools.


The platform comes with interconnected **out\-of\-the\-box
add\-ons** for report generation, BPM, maps, instant web app
generation from a DB, and quite a bit more:


**[\&gt;\&gt; Become an efficient
full\-stack developer with Jmix](/jmix-haulmont-NPI-EA-37efg)**



Baeldung Pro – NPI EA (cat \= Baeldung)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

Baeldung Pro comes with both absolutely **No\-Ads** as well as
finally with **Dark Mode**, for a clean learning experience:


[\&gt;\&gt; Explore a clean
Baeldung](/baeldung-pro-NPI-EA-trpcd)


Once the early\-adopter seats are all used, **the price will go
up and stay at $33/year.**



eBook – Java Concurrency – NPI EA (cat\=Java Concurrency)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

Handling concurrency in an application can be a tricky process
with many **potential pitfalls**. A solid grasp of the
fundamentals will go a long way to help minimize these issues.


Get started with understanding multi\-threaded applications with
our **Java Concurrency** guide:


[\&gt;\&gt; Download
the eBook](/eBook-java-concurrency-NPI-EA-24dy0)



Partner – Orkes – NPI EA (tag \= Microservices)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

Modern software architecture is often broken. Slow delivery
leads to missed opportunities, innovation is stalled due to
architectural complexities, and engineering resources are
exceedingly expensive.


**Orkes is the leading workflow orchestration platform**
built to enable teams to transform the way they develop, connect,
and deploy applications, microservices, AI agents, and more.


With Orkes Conductor managed through Orkes Cloud, developers can
focus on building mission critical applications without worrying
about infrastructure maintenance to meet goals and, simply put,
taking new products live faster and reducing total cost of
ownership.


**Try a [14\-Day
Free Trial of Orkes](/orkes-NPI-EA-3Dm8K) Conductor today.**



Partner – Microsoft – NPI EA (cat \= Spring Boot)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

Azure Container Apps is a fully managed serverless container
service that enables you to **build and deploy modern,
cloud\-native Java applications and microservices** at scale. It
offers a simplified developer experience while providing the
flexibility and portability of containers.


Of course, Azure Container Apps has really solid support for our
ecosystem, from a number of build options, managed Java components,
native metrics, dynamic logger, and quite a bit more.


To learn more about Java features on Azure Container Apps, visit
the [documentation
page](/microsoft-NPI-EA-8BnN2).


You can also ask questions and leave feedback on the Azure
Container Apps [GitHub page](/microsoft-NPI-EA-9jJ51).



Partner – Machinet – NPI EA (cat \= Baeldung)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

The AI Assistant to boost Boost your productivity writing unit
tests \- **Machinet AI**.


AI is all the rage these days, but for very good reason. The
highly practical coding companion, you'll get the power of
AI\-assisted coding and **automated unit test generation**.  

Machinet's **Unit Test AI Agent** utilizes your own project
context to create meaningful unit tests that intelligently aligns
with the behavior of the code.  

And, the **AI Chat** crafts code and fixes errors with ease,
like a helpful sidekick.  



Simplify Your Coding Journey with **Machinet AI**:


**[\&gt;\&gt;
Install Machinet AI in your IntelliJ](/Machinet-NPI-EA-fl9ht)**



Partner – Codium – NPI EA (cat \= Testing)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

Explore the secure, reliable, and high\-performance Test
Execution Cloud built for scale. Right in your IDE:


**[\&gt;\&gt;
CodiumAI. Meaningful Code Tests for Busy Devs](/codium-NPI-EA-A4d5b)**


Basically, write code that works the way you meant it to.



Partner – Machinet – NPI EA (cat \= Testing)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

AI is all the rage these days, but for very good reason. The
highly practical coding companion, you'll get the power of
AI\-assisted coding and **automated unit test generation**.  

Machinet's **Unit Test AI Agent** utilizes your own project
context to create meaningful unit tests that intelligently aligns
with the behavior of the code.  



Simplify Your Coding Journey with **Machinet AI**:


**[\&gt;\&gt;
Install Machinet AI in your IntelliJ](/Machinet-NPI-EA-2mrw!)**



eBook – Persistence – NPI EA (cat\=Persistence)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

Working on getting your persistence layer right with Spring?


[Explore the eBook](/ebook-persistence-NPI-EA-35epd)



eBook – Java Streams – NPI EA (cat\=Java Streams)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

Since its introduction in Java 8, the Stream API has become a
staple of Java development. The basic operations like iterating,
filtering, mapping sequences of elements are deceptively simple to
use.


But these can also be overused and fall into some common
pitfalls.


To **get a better understanding on how Streams work** and how
to combine them with other language features, check out our guide
to Java Streams:


[\&gt;\&gt;Download the
E\-book](/eBook-Java-Streams-NPI-EA-fcdg2)



eBook – HTTP Client – NPI EA (cat\=HTTP Client\-Side)![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)  

The **Apache HTTP Client** is a very robust library, suitable
for both simple and advanced use cases when **testing HTTP
endpoints**. Check out our guide covering basic request and
response handling, as well as security, cookies, timeouts, and
more:


[\&gt;\&gt; Download the
eBook](/ebook-http-client-NPI-EA-3jcsr)



Course – LS – NPI EA (cat\=REST)  

![announcement - icon]()![announcement - icon](/wp-content/uploads/2022/04/announcement-icon.png)
**Get started with Spring Boot** and with core Spring,
through the *Learn Spring* course:


**[\&gt;\&gt; CHECK OUT THE
COURSE](/course-ls-NPI-EA-b@hh6)**



 







 




 
 
 





![The Baeldung logo](https://www.baeldung.com/wp-content/themes/baeldung/icon/logo.svg)


#### Courses

* [All Courses](/courses/all-courses)
* [Baeldung All Access](/courses/all-access)
* [Baeldung All Team Access](/courses/all-access-team)
* [The Courses Platform](https://courses.baeldung.com)
#### Series

* [Java “Back to Basics” Tutorial](/java-tutorial)
* [Jackson JSON Series](/jackson)
* [Apache HttpClient Series](/httpclient-series)
* [REST with Spring Series](/rest-with-spring-series)
* [Spring Persistence Series](/persistence-with-spring-series)
* [Security with Spring](/security-spring)
* [Spring Reactive Series](/spring-reactive-series)
#### About

* [About Baeldung](/about)
* [The Full Archive](/full_archive)
* [Editors](/editors)
* [Our Partners](/partners/)
* [Partner with Baeldung](/partners/work-with-us)
* [eBooks](/library/)
* [FAQ](https://www.baeldung.com/library/faq)
* [Baeldung Pro](/members/)
 

* [Terms of Service](/terms-of-service)
* [Privacy Policy](/privacy-policy)
* [Company Info](/baeldung-company-info)
* [Contact](/contact)
 

![The Baeldung Logo](https://www.baeldung.com/wp-content/themes/baeldung/icon/whiteleaf.svg)

 
 
 
 
 















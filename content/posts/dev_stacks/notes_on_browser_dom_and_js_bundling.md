---
date: 2024-04-01
title: "In depth understanding of Browser, DOM, and JavaScript Bundling"
---



## 1. How a File Server Communicates with a Browser

### Where doe the browser get its files?
- Think of a browser like a little server that keeps asking for files.
- it communicates with another server for files. this 'another server' is why we run `npm serve` (creates a file server).
- the file server sends files over HTTP.
- Now comes the question, 
  - **Q1** how does a browser know what files it needs?
  - **Q2** how does the file server know where to get those files?

### **Q1 Answer**: How the browser get its files
- When you start a file server in your project directory (`./`), it listens on a specific ip (`127.0.0.1`) and port (`:3000`) for incoming HTTP requests (`http://`). this is why you put `http://localhost:3000` in the browser as url.
- once you put in the url, the browser knows where to ask for files, so it sends an HTTP GET request to the server for the root document (usually `index.html`).
- The server got the request so it responds with the asked file.
-  As the browser parses `index.html` (into a DOM, explained later), it may find it need more files (CSS, JavaScript files, images). It sends more GET request for those files as well. (explained in Q3)
-  So **Q3** how does the browser creates a website we see using all these files exactly?

### **Q2 Answer**: How the file server find the files
- It's simple in concept: if the browser asks for `/index.html`, the server looks for `./index.html` in the project's root directory. 
- However, the reality becomes more complex with the use of JavaScript modules, especially when dealing with dependencies stored in `node_modules`.
- When your JavaScript code uses modules, such as importing React with `import React from 'react';`, both the browser and the basic file server face a challenge. The browser doesn't inherently know where `react` is located within `node_modules`, nor does a simple file server know how to resolve this import without explicit instructions. Manually specifying the path for each module, like `"./node_modules/react/index.js"`, quickly becomes impractical as the number of dependencies grows.
- This manual configuration of paths for potentially thousands of files is unrealistic in the modern `JavaScript/Node.js` ecosystem. 
- There needs to be a system that automatically manages these dependencies and communicates their locations to both developers and the server. 
- This is where bundlers, such as `Webpack` and `Parcel`, come into play. **Q6** How do bundlers know where to look for files and inform the file server about these locations?

### **Q3 Answer**: How the browser converts static files to a dynamic website
- Once the browser receives `index.html` from the server, it begins the process of building the web page. 
- This involves several steps:
  - First, The browser reads through (parsing) the `index.html` file, incrementally creating an in-memory representation of the websites's structure (called the DOM). Each element in the HTML file corresponds to a node in the DOM tree. ![](/images/Document Object Model.png)
  - As the parser encounters tags linking to external resources (like `<script src="index.js"></script>`, or `css`, or `jpg`, etc), it makes additional HTTP GET requests to the server for each resource.
  - Notice how resource is loading **while** DOM building -- This is called Dynamic Loading, which differes from Static Loading where all resources are loaded before DOM building.
  - **loading javascript**: `async` or `defer` keyword in `<script>` tags will indicate a `non-blocking` loading of the script, otherwise the browser would wait for it to load before proceed (which could be necessary for some resources). `defer` means run after DOM construction whereas `async` means run in parallel with DOM construction. this leads to an interesting feature of Javascript: **Q4** How does a single-threaded language handle `non-blocking`?
  - **loading css**: loaded `async` (in parallel with DOM construction). However, rendering only starts after CSSOM is ready. **Q5** What is CSSOM and how does it connect to everything else?
- After the DOM and CSSOM is constructed, the browser combines them to create the Render Tree. (which is the static representation of the website at that time point) Notice render tree does not include `display: none` elements (they are in DOM though).
- Next is the Layout calculation: (also known as "reflow") the browser traverses the render tree to decide the position and dimention of each element. (it traverses both DOM for hierarchical structure and CSSOM for visual properties)
- Finally, the browser starts "painting" the screen. painting is just filling pixels by drawing out text colors, images, borders, etc. based on the layout calculation.

### **Q4 Answer** `Event Loop` and `Task Management` -- how single-thread mimics multi-thread
- The browser manages task like parsing html, executing javascript, fetching resources, etc through the Event loop and various task queues.
- What are **Task Queues**: 
  - Just like normal queues, when there is more task than browser can handle, it queues them up for later.
  - There are multiple queues, like `task queue` for most events (clicks, network events, etc), `microtask queue` for promises, and mutation obeserver: which keep track of changes in DOM. (when a node is changed a callback is added to the queue to enforce the change)
- What is a **Event Loop**:
  - The event loop is the routine that prioritizes tasks in different task queues and executes them one by one.
  - basically when we say `single-thread`, this is the thread we are talking about.
  - It prioritizes promises (microtask) queue over task queue (finsh micro before macro).
- the **call stack** and **execution context**:
  - each task creates an execution context like variable allocations and function declarations. 
  - the call stack is where all the context is stored.

### **Q5 Answer** CSSOM
- CSSOM is the CSS Object Model, which is a hierarchy of css rules generated from css files. ![](/images/CSSDOM.png)
- the CSSOM mirros DOM's structure, but it only store css rules.
- The tree structure creates a hirearchy so rules can cascade from root to all nodes.
- When the browser builds the CSSOM and decide which css rule to apply first, It considers: cascade, specificity, and source order of CSS rules:
  - Then it constructs the CSSOM by reading and parsing the CSS rules, creating a structured representation of these rules.
  - The css rules may come from all sources (external stylesheets, `<style>` elements, inline styles, and browser default styles)
  - `Cascade` and `Specificity`: As it constructs the CSSOM, the browser applies the CSS cascade and specificity rules. This means that it considers:
    - The importance of a rule (e.g., `!important` declarations).
    - The specificity of the selector (inline styles, IDs, classes, and elements (like `<h1>`), in decreasing order of specificity).
    - The source order of CSS rules, with later rules overriding earlier ones if specificity is equal.
    - higher specificity, less likely to be overridden. (means if you do inline, its almost certain to be applied)
    - in summary: `!important` triumphs all, specificity is considered 

### **Q6 Answer** How bundlers know where to look for files and inform the file server
1. starting from index.js, the bundler starts to investigate what dependency script it has (create a dependency graph) (side note: if configured, bundlers can also check for css, images, html, etc, for example, generating multiple resolution of images can be done by bundler)
2. for each dependency found, the bundler check project root first, then `package.json`.
3. Next is loading those files. it read the file, transform the file according to users needs (like polyfills, `ts` to `js`, `scss` to `css`, etc)
4. with all the source file ready the bundler then, optionally, minify, treeshake, etc to reduce file size, then all these files are stacked together (by removing the import clause and wrap a module into a function to preserve scope) into a few files.
5. finally bundled files are saved to specified location and file servers can get read to serve them to browsers. bundlers could also come with a development server so hot update is more seamless. 
6. **Problems with bundlers**
   - setup is too complex, configuration is too much
   - larger projects takes very long to build due to all the things bundlers do (and more computing power)
   - need developement setting, then production setting, then testing setting, even more work.
   - So **Q7** How do ES modules and Vite solve these problems?

### **Q7 Answer** ES modules and Vite
- sensible defaults reduce setup time
- By using ES modules, Vite serve code directly to the browser (no bundling) and let the browser handle the dependency graph.
- Hot Module Replacement (HMR): no rebundling just serve.
- Dev and Prod parity: it try to reduce dependencies so the setting is almost the same.
- Since no bundling, it caches the file so later loading is even faster.
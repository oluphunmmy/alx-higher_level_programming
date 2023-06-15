JavaScript - Objects, Scopes and Closures

JavaScript object basics
An object is a collection of related data and/or functionality. These usually consist of several variables and functions (which are called properties and methods when they are inside objects).

Object prototypes
Prototypes are the mechanism by which JavaScript objects inherit features from one another
Every object in JavaScript has a built-in property, which is called its prototype. The prototype is itself an object, so the prototype will have its own prototype, making what's called a prototype chain. The chain ends when we reach a prototype that has null for its own prototype.

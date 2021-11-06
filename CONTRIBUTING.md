# Developing Cadence

This doc is intended for contributors to `cadence` client (hopefully that's you!)

Join our Slack channel(invite link in the [home page](https://github.com/uber/cadence#cadence)) #development if you need help.
>Note: All contributors need to fill out the [Uber Contributor License Agreement](http://t.uber.com/cla) before we can merge in any of your changes

## Development Environment
Below are the instructions of how to set up a development Environment.

### 1. Building Environment

* Python. Make sure you are running python version between 3.5-3.8 (3.9 gives an error with the thrift library that we're currently deprecating).
If you have a different python version in your local system, we suggest using [pyenv](https://github.com/pyenv/pyenv)

* Download project dependencies and dev dependencies.
```bash
$ pip install -r requirements.txt
$ pip install -r dev-requirements.txt
```

### When to open a PR
You have a few options for choosing when to submit:

* You can open a PR with an initial prototype with "Draft" option or with "WIP"(work in progress) in the title. This is useful when want to get some early feedback.

* PR is supposed to be or near production ready. You should have fixed all styling, adding new tests if possible, and verified the change doesn't break any existing tests.

* For small changes where the approach seems obvious, you can open a PR with what you believe to be production-ready or near-production-ready code. As you get more experience with how we develop code, you'll find that more PRs will begin falling into this category.

### Commit Messages And Titles of Pull Requests

Overcommit adds some requirements to your commit messages. At Uber, we follow the
[Chris Beams](http://chris.beams.io/posts/git-commit/) guide to writing git
commit messages. Read it, follow it, learn it, love it.

All commit messages are from the titles of your pull requests. So make sure follow the rules when titling them.
Please don't use very generic titles like "bug fixes".

All PR titles should start with UPPER case.


### Code review
We take code reviews very seriously at Cadence. Please don't be deterred if you feel like you've received some hefty feedback. That's completely normal and expected—and, if you're an external contributor, we very much appreciate your contribution!

In this repository in particular, merging a PR means accepting responsibility for maintaining that code for, quite possibly, the lifetime of Cadence. To take on that reponsibility, we need to ensure that meets our strict standards for production-ready code.

No one is expected to write perfect code on the first try. That's why we have code reviews in the first place!

Also, don't be embarrassed when your review points out syntax errors, stray whitespace, typos, and missing docstrings! That's why we have reviews. These properties are meant to guide you in your final scan.

### Addressing feedback
If someone leaves line comments on your PR without leaving a top-level "looks good to me" (LGTM), it means they feel you should address their line comments before merging.

You should respond to all unresolved comments whenever you push a new revision or before you merge.

Also, as you gain confidence in Python, you'll find that some of the nitpicky style feedback you get does not make for obviously better code. Don't be afraid to stick to your guns and push back. Much of coding style is subjective.

### Merging
External contributors: you don't need to worry about this section. We'll merge your PR as soon as you've addressed all review feedback(you will get at least one approval) and pipeline runs are all successful(meaning all tests are passing).


### Useful shortcuts

We created a Makefile our life easier when developing


#make generate-grpc-code

It will generate the most up-to-date gRPC client and server interfaces from the cadence .proto service definition (located at `idls`)



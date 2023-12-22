- For all .html files of your project, please put those in a /template folder. This has to do with how some things in the code work otherwise, basically.
- Put adscript.js in a /static folder. This has to do with how some things in the code work otherwise, basically.
- Put images in a /static/images folder path.

There's a requirements.txt file to help with deployment. If you're using Visual Studio for coding, if you want to make a requirements.txt document to see if that helps with some troubleshooting, you can go to the terminal and use pip freeze > requirements.txt, assuming that Python is installed.

The current version only has scope to recognize an article that has a car, carrot, or parrot as the main topic, except a default image with the word pizza in it can show if there's issue with finding one of those keywords. In the future, more nouns can be added to the list of keywords.

There's a plan for there to be more documentation later. Basically, this project is meant to be for a privacy focused ads, where the program reads some content on a page and outputs an image. The image will be the advertisement.

This first version is what I view as a minimum viable product to show the concept.

## Acknowledgements

This project makes use of [SpaCy](https://spacy.io/), an open-source software library for advanced natural language processing. SpaCy is developed and maintained by Explosion and is licensed under the MIT License. The original license text for SpaCy can be found [here](https://github.com/explosion/spaCy/blob/master/LICENSE).

### SpaCy License

MIT License

Copyright (c) [year] Explosion

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Using ChatGPT in a custom action to answer questions about data


Most Rasa chatbots fetch data from an API. E.g. in the financial-demo, a user can see their latest transactions.
Here, we have a dummy API returning restaurant results.

Using the ChatGPT API, we then allow users to ask questions *about* the data they've just been shown. 
We have an existing feature called [Knowledge Base Actions](https://rasa.com/blog/integrating-rasa-with-knowledge-bases/) which does the same thing. In comparison, using ChatGPT is much simpler, but also occasionally makes up wrong answers!


<img width="1173" alt="image" src="https://user-images.githubusercontent.com/5114084/222745358-84140a22-12c6-493e-b66e-0c94a20afec0.png">


Here's the data which the API has access to:

|    | Restaurants            |   Rating | Has WiFi   | cuisine   |
|---:|:-----------------------|---------:|:-----------|:----------|
|  0 | Mama's Pizza           |      4.5 | False      | italian   |
|  1 | Tacos el Cabron        |      4.6 | True       | mexican   |
|  2 | China Palace           |      3.2 | False      | chinese   |
|  3 | The Cheesecake Factory |      4.2 | True       | american  |
|  4 | Pizza Hut              |      3.8 | True       | italian   |
|  5 | Biryani Bowl           |      4.9 | False      | indian    |
|  6 | Burger King            |      2.6 | True       | american  |
|  7 | Taco Bell              |      3.5 | True       | mexican   |
|  8 | Freshii                |      4.7 | True       | healthy   |
|  9 | Panda Express          |      3.9 | False      | chinese   |
| 10 | McDonald's             |      2.3 | True       | american  |
| 11 | Sushi Roku             |      4.8 | True       | japanese  |
| 12 | Olive Garden           |      4   | True       | italian   |
| 13 | Chipotle               |      4.4 | True       | mexican   |
| 14 | Little Caesars         |      3.1 | False      | italian   |

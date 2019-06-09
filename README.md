My graduation theses

Department of Cybernetics and Artificial Intelligence, Faculty of Electrical Engineering and Informatics, Technical University of Košice, Letná 9, 042 00 Košice, Slovakia

This work aims to understand and process data about NHL players. 
With data, we create a prediction model to players salary. 
The full analytical process will be implemented with the CRISP-DM in Python. 
With Feature selection we find the most influencing attributes, with Stepwise regression we find the best combina-tion of attributes.
And with Polynomial regression, we calculate the final model. 
From multiple iterations, we choose the best model. 
This model used a support application. 
This application will be created using a combination of R and Python programming languages. 
The final version of the app will be tested and evaluated user testing.

Business understanding

Our goal was to create multiple models that will predict the salary of NHL players. 
From these models, we choose the best one with the potential to be deployed into practice in the form of a web application. 
From the analytical point of view, we aimed at a selection of the most important attributes affecting the players’ salary and based on this selection; we applied the regression algorithms.

Data Preparation

Most of the attributes are of numeric type. 
Nominal types are BIO attributes such as name, surname or country. 
We divided the goalie's stats into ten and player’s stats into 12 categories by the same characteristics. 
In the beginning, the number of attrib-utes was high and therefore, depending on the correlation between them, we started their reduction. 
  For example, the pairs of attributes like iFOW – Fow.Up, G.Tip – G.Wrap, iPent – iPENT or Misc – G.Misc represents a situation that one of them is calculated from the value of the second. 
We also used the Bayesian information criterion (BIC) to remove less-important categories and keep only relevant data.
Next, we needed to synchronize the attribute names and to determine one measur-ing unit. 
Also, we have removed all players and goalies that have played 9 or fewer matches. 
Then we created new 12 attributes based on existing data. 
Next, we divided the data into nine tables by type of contract and by the player's position. 
Goalies data was split into three small sub files by contract type to RFA (restricted free agents), UFA (unrestricted free agents) and rookie categories with salary less than 1 million.
Player attributes were initially divided by position, namely to the defenders and the forwards. 
Then again by contract type to UFA, RFA and rookie with salary less than 1 million. 
Overall, we have 9 data files. The goalies samples contained 47 columns and 62-261 rows, the players’ data 59 attributes and 308-1423 rows (play-ers). 


Finally, we calculated the importance of all numerical attributes relative to the target attribute (CapHit). 
For this purpose, we used the univariate attribute selection that selecting the best attributes based on univariate statistical tests.
The calculation uses the SelectorKBest class, which determines the number of best attributes in com-bination with suitable statistical test. We have applied this process to two basic types of data for a set of all players and a set of all goalies without a split. 

And the results were:

•	Top 5 goalies attributes: Wt (weight), HT (height), PPSA (power play shots against), GAA (goals against average), SHSA (shorthanded shot against).

•	Top 5 players attributes: Wt (weight), HT (height), TOI/G (time on ice per game), Shift/G (shifts per game), TOI (time on ice). 

Also, we applied the Sequential Forward Selection to identify the most im-portant attributes. 
Sequential Feature Selector algorithms are a family of greedy search algorithms. 
These algorithms add or remove one attribute at the time based on the classifier performance until a variables subset of the desired size is reached. We obtained the following results:

•	Top 16 goalies attributes: GS, OT, GR, MIN, SO, StMIN, StSV%, StGAA, QS, ReMIN, SHSV%, PPSV%, SOW, SOL, SSA and, SGA (the prediction accuracy only 54%, but the best from the all related experiments).

•	Top 8 players attributes: HT, Wt, TOI/G, A/G, PIM/G, Shifts/G, Diff/G and Bl/G (the prediction accuracy 67%).

The results were in some cases the same, but most of the selected attributes were different. 
Attributes selected by SFS algorithm were more trusted.

Modeling and Evaluation

We used the preprocessed data as an input to calculate the models within the polynomial regression method. 
First, we calculated the anticipated CapHit for all goalkeeper and all players without a split. 
For the category of all goalies, the model's precision exceeded 95%, which is a perfect result. 
But for all players, it was only about 54%, which is too low. 
Also, we used polynomial regression to calculate the expected salary for all divided tables

Table	        Score

GoaliesN	    0.84798	

GoaliesU	    0.79729	

GoaliesR	    0.84776	

DefensemanN	    0.54302	

DefensemanU	    0.53995	

DefensemanR	    0.92464

ForwardN	    0.41503

ForwardU	    0.82917

ForwardR	    0.71461

Goalies	        0.95469

Forward	        0.54339

As we can see from the table, for all three goalie categories, we were less accurate than the total set of all goalies. 
But in three cases the players were more precision than all the players, and the other three were not the best. 
Especially in the case of the rookie, we have no very suitable models.

Deployment

After evaluation, we designed and implemented the supporting application using all obtained knowledge and experienced from the previous parts of the analytical process. We aimed to offer simple, understandable user interface with all necessary analytical functions. The first tab presents basic information about the application; the second one contains an overview of all input attributes and their explanations. The next offers a simple visualization of available data and a summarization of the models. The last card provides the salary prediction visualized as a graph comparing the real and predicted value.
The final version of the app was evaluated by user acceptance testing. We focused this testing on following factors related to the quality of the web applications : functionality, appearance, performance, error rate and rememberability.  The users were people who are very well versed in the NHL. The results showed that 78.3% of the participants were satisfied with the content of the application; 70% of them praised the graphics. They did not identify any significant errors during the testing scenarios. After one week, the testers improved their results. Finally, they proposed some ideas on how we can improve our app.

App is created in Slovak language and will be created in R. 
App is available online for:
https://prostats-mg-dp.shinyapps.io/dp_mg_app/

Conclusion

We aimed to understand and process data about NHL players to predict the player's salary. We used the best model and obtained experiences for creating the supporting application. This application offers the functionalities in a simple, understandable form. We know that the generated models are not perfect, but users can use them as support for their decision in offering / accepting contracts. Based on performed state-of-the-art (Matt Cane - hockey analytics researcher, Cameron Nugent – PhD. student and data scientist, Kevin Peck – honors thesis, Stefan Nordenskjöld and Carl Flogvall – bachelor thesis) we can state that our application is the first one solving this task from a more complex perspective. However, the final model we have created is still not in perfect shape. Meanwhile, he can act as a consultant in offering / accepting contracts. However, this model needs to be constantly improved by adding new in-formation that influences the salary of players.

The work was partially supported by the Slovak Grant Agency of the Ministry of Education and Academy of Science of the Slovak Republic under grant no. 1/0493/16 and The Slovak Research and Development Agency under grant no. APVV-16-0213.

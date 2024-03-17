
## Design choices

#### Do I need to delete the from db when deleting?
- _soft deletion by default, unless there's some reason not to._ [Senior Engineer](https://news.ycombinator.com/item?id=32156009)
- There is no reason to delete the row, we don't know what will happen, especially 
it's a financial data so will do a soft delete

## Challenges

#### What does req.txt mean in Python ?
- It's file that contains all libraries and dependancies in the project, so that the other contributers can install it with no conflicts

#### What does this folder structur mean (api, controler, db, resource)?
- its a popular folder structre with FastAPI
- recourese [Article](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

#### What does __init__ file mean ?
- This is what allows importing code from one file into another.


#### Should i use request library or http.client ?
- http.client a standard library from Python (less intuitive, more control)
- Reqest external library (Readable and concise)
- I'll go with request, because its simple


#### What is the naming convesion for function ?
- snake_case [the Style Guide for Python Code](https://pep8.org/)

#### How can i handle the enviroment varialbes ?
- [Python Environment Variables](https://developer.vonage.com/en/blog/python-environment-variables-a-primer)

#### How can i handle errors when sending a request ?
- [Exception Handling Best Practices](https://www.slingacademy.com/article/python-requests-exception-handling-best-practices/)

#### How can i import packages and subpackages ?
- [stackoverflow](https://stackoverflow.com/questions/71449587/importing-packages-and-subpackages-in-python)

#### ORM and connecting to DB
- [Cockroach docs](https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-sqlalchemy)
- [SQlAlcemy docs](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html)
- [Toturial] (https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_connecting_to_database.htm)

#### What does double underscore (__) mean ?
- **Single leading underscore:**  internal use only
- **Single trailing underscore:** Avoids naming conflicts with Python keywords
- **Double leading underscore:** Triggers name mangling 
- **Double leading and trailing underscore:** special attributes and methods that Python provides
- **Single underscore:** temporary variable
- [Article](https://realpython.com/python-double-underscore/)

#### What is the difference between list and array ?
- List: different types
- Array: same type

#### FastAPI resources
- [Docs](https://fastapi.tiangolo.com/tutorial/body-fields/)
- [How to Use FastAPI](https://www.youtube.com/watch?v=SORiTsvnU28)

#### RabbitMQ resources
- [Hussain Nasser (Crash Course)](https://youtu.be/Cie5v59mrTg?si=kzv--8jM_HIMsYbh)
- [What is a Message Queue and When should you use Messaging Queue Systems](https://youtu.be/W4_aGb_MOls?si=4SufosdHeIaz2xXR)

#### Meaning of if __name__ == "__main__"
- Code will only be executed if the script is run as the main program
- [Article](https://www.theserverside.com/tip/What-does-the-Python-if-name-equals-main-construct-do#:~:text=to%20the%20console.-,The%20if%20__name__%20%3D%3D%20%22__main__%22%3A,it%20would%20not%20execute%20automatically.)

#### What does Event Looping means?


----
### TODO: 
- Open a pr to fix bugs 
  - naming under resources folder
  - error article comma
  
<br> <br>

- [ ] improve the error handling
- [ ] write a proper comments for the documentation
- [ ] select only needed columns
- [x] make sure to use pydantic models in all responses
- [ ] implement a proper logging
- [ ] populate threshold_exceeded when creating a new rule
- [ ] store market data in the db

-----
### Thinking:
- i'll have two things (symbol, current_price, threshold_price)
- the event will trigger with these three things, and the event will be a message in the queue
- then the consumer will consume the message and will do two things:
  - print the message
  - insert into alert table


market_data
{
  "symbol": "AAPL",
  "price": 100,
}

rules
{
  {
  "symbol": "AAPL",
  "threshold": 120,
  ""
  }
}
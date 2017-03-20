Quick Start Full Example
Save this example in api.py

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
Example usage

$ python api.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
GET the list

$ curl http://localhost:5000/todos
{"todo1": {"task": "build an API"}, "todo3": {"task": "profit!"}, "todo2": {"task": "?????"}}
GET a single task

$ curl http://localhost:5000/todos/todo3
{"task": "profit!"}
DELETE a task

$ curl http://localhost:5000/todos/todo2 -X DELETE -v

> DELETE /todos/todo2 HTTP/1.1
> User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3
> Host: localhost:5000
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 204 NO CONTENT
< Content-Type: application/json
< Content-Length: 0
< Server: Werkzeug/0.8.3 Python/2.7.2
< Date: Mon, 01 Oct 2012 22:10:32 GMT
Add a new task

$ curl http://localhost:5000/todos -d "task=something new" -X POST -v

> POST /todos HTTP/1.1
> User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3
> Host: localhost:5000
> Accept: */*
> Content-Length: 18
> Content-Type: application/x-www-form-urlencoded
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 25
< Server: Werkzeug/0.8.3 Python/2.7.2
< Date: Mon, 01 Oct 2012 22:12:58 GMT
<
* Closing connection #0
{"task": "something new"}
Update a task

$ curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v

> PUT /todos/todo3 HTTP/1.1
> Host: localhost:5000
> Accept: */*
> Content-Length: 20
> Content-Type: application/x-www-form-urlencoded
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.8.3 Python/2.7.3
< Date: Mon, 01 Oct 2012 22:13:00 GMT
<
* Closing connection #0
{"task": "something different"}



update	 $ curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v
add 	 $ curl http://localhost:5000/todos -d "task=something new" -X POST -v
delete	 $ curl http://localhost:5000/todos/todo2 -X DELETE -v
get 	 $ curl http://localhost:5000/todos






//return object
Data Formatting
By default, all fields in your return iterable will be rendered as-is. While this works great
 when you’re just dealing with Python data structures, it can become very frustrating when working
 with objects. To solve this problem, Flask-RESTful provides the fields module and 
 the marshal_with() decorator. Similar to the Django ORM and WTForm, you use the fields module
 to describe the structure of your response.

from collections import OrderedDict
from flask_restful import fields, marshal_with

resource_fields = {
    'task':   fields.String,
    'uri':    fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')
The above example takes a python object and prepares it to be serialized. 
The marshal_with() decorator will apply the transformation described by resource_fields.
The only field extracted from the object is task. 
The fields.Url field is a special field that takes an endpoint name and generates a URL for that endpoint in the response. 
Many of the field types you need are already included. See the fields guide for a complete list.







//输出字段//field
Flask-RESTful 提供了一个简单的方式来控制在你的响应中实际呈现什么数据。使用 fields 模块，
你可以使用在你的资源里的任意对象（ORM 模型、定制的类等等）并且 fields 让你格式化和过滤响应，
因此您不必担心暴露内部数据结构。

>>>for extend

You can define a dict or OrderedDict of fields whose keys are names of attributes or keys on the object to render, 
and whose values are a class that will format & return the value for that field.

from flask_restful import Resource, fields, marshal_with

resource_fields = {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
}

class Todo(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, **kwargs):
        return db_get_todo()  # Some function that queries the db
The decorator marshal_with is what actually takes your data object and applies the field filtering.
 The marshalling can work on single objects, dicts, or lists of objects.

Note
marshal_with is a convenience decorator, that is functionally equivalent to

class Todo(Resource):
    def get(self, **kwargs):
        return marshal(db_get_todo(), resource_fields), 200
		
		
----------------------------------------------------------------		
class UrgentItem(fields.Raw):
    def format(self, value):
        return "Urgent" if value & 0x01 else "Normal"

class UnreadItem(fields.Raw):
    def format(self, value):
        return "Unread" if value & 0x02 else "Read"

fields = {
    'name': fields.String,
    'priority': UrgentItem(attribute='flags'),
    'status': UnreadItem(attribute='flags'),
}

restful api //Renaming Attributes field
-----------------------------------------------------------------

//Renaming Attributes
Often times your public facing field name is different from your internal field name. To configure this mapping, use the attribute keyword argument.

fields = {
    'name': fields.String(attribute='private_name'),
    'address': fields.String,
}

A lambda (or any callable) can also be specified as the attribute

fields = {
    'name': fields.String(attribute=lambda x: x._private_name),
    'address': fields.String,
}

Nested properties can also be accessed with attribute

fields = {
    'name': fields.String(attribute='people_list.0.person_dictionary.name'),
    'address': fields.String,
}


//Default Values
If for some reason your data object doesn’t have an attribute in your fields list, you can specify a default value to return instead of None.

fields = {
    'name': fields.String(default='Anonymous User'),
    'address': fields.String,
}

//multivalue              “attribute=”    是与obj对接的
This example assumes that bit 1 in the flags attribute signifies a “Normal” or “Urgent” item, 
and bit 2 signifies “Read” or “Unread”. These items might be easy to store in a bitfield, 
but for a human readable output it’s nice to convert them to seperate string fields.

class UrgentItem(fields.Raw):
    def format(self, value):
        return "Urgent" if value & 0x01 else "Normal"

class UnreadItem(fields.Raw):
    def format(self, value):
        return "Unread" if value & 0x02 else "Read"

fields = {
    'name': fields.String,
    'priority': UrgentItem(attribute='flags'),
    'status': UnreadItem(attribute='flags'),
}


如果fields里的值与obj.Attributes相同，则辨识出对应值被fields.String输出
如果不同，则为新加的数据，上例，下例 # 'uri': fields.Url('todo_resource'),

This is also a good example of how to add data to your response that’s not actually present on your data object.:

class RandomNumber(fields.Raw):
    def output(self, key, obj):
        return random.random()

fields = {
    'name': fields.String,
    # todo_resource is the endpoint name when you called api.add_resource()
    'uri': fields.Url('todo_resource'),
    'random': RandomNumber,
}


//Complex Structures
You can have a flat structure that marshal() will transform to a nested structure

>>> from flask_restful import fields, marshal
>>> import json
>>>
>>> resource_fields = {'name': fields.String}
>>> resource_fields['address'] = {}
>>> resource_fields['address']['line 1'] = fields.String(attribute='addr1')
>>> resource_fields['address']['line 2'] = fields.String(attribute='addr2')
>>> resource_fields['address']['city'] = fields.String
>>> resource_fields['address']['state'] = fields.String
>>> resource_fields['address']['zip'] = fields.String
>>> data = {'name': 'bob', 'addr1': '123 fake street', 'addr2': '', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
>>> json.dumps(marshal(data, resource_fields))
'{"name": "bob", "address": {"line 1": "123 fake street", "line 2": "", "state": "NY", "zip": "10468", "city": "New York"}}'
Note
The address field doesn’t actually exist on the data object, 
but any of the sub-fields can access attributes directly from the object as if they were not nested.

















prototype1 client

import requests,json
# requests.get('http://localhost:5000/tasks').json()
requests.post('http://127.0.0.1:5000/tasks',
                  headers={'Content-Type': 'application/json'},
                  data=json.dumps({'tracknumber': '111111'}))



# requests.put('http://127.0.0.1:5000/tasks/test-20151019142043-jack-newtest',
#                 headers={'Content-Type': 'application/json'},
#                 data=json.dumps({'status': '1'})).json()
#
# requests.delete('http://localhost:5000/tasks/222')






什么是 REST？
六条设计规范定义了一个 REST 系统的特点:

客户端-服务器: 客户端和服务器之间隔离，服务器提供服务，客户端进行消费。
无状态: 从客户端到服务器的每个请求都必须包含理解请求所必需的信息。换句话说， 服务器不会存储客户端上一次请求的信息用来给下一次使用。
可缓存: 服务器必须明示客户端请求能否缓存。
分层系统: 客户端和服务器之间的通信应该以一种标准的方式，就是中间层代替服务器做出响应的时候，客户端不需要做任何变动。
统一的接口: 服务器和客户端的通信方法必须是统一的。
按需编码: 服务器可以提供可执行代码或脚本，为客户端在它们的环境中执行。这个约束是唯一一个是可选的。



-------------------------------------------------------------------------------
确保我们的 web service 安全服务的最简单的方法是要求客户端提供一个用户名和密码。在常规的 web 应用程序会提供一个登录的表单用来认证，并且服务器会创建一个会话为登录的用户以后的操作使用，会话的 id 以 cookie 形式存储在客户端浏览器中。然而 REST 的规则之一就是 “无状态”， 因此我们必须要求客户端在每一次请求中提供认证的信息。

我们一直试着尽可能地坚持 HTTP 标准协议。既然我们需要实现认证我们需要在 HTTP 上下文中去完成，HTTP 协议提供了两种认证机制: Basic 和 Digest。

有一个小的 Flask 扩展能够帮助我们，我们可以先安装 Flask-HTTPAuth:

$ flask/bin/pip install flask-httpauth
比方说，我们希望我们的 web service 只让访问用户名 miguel 和密码 python 的客户端访问。 我们可以设置一个基本的 HTTP 验证如下:

from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
get_password 函数是一个回调函数，Flask-HTTPAuth 使用它来获取给定用户的密码。在一个更复杂的系统中，这个函数是需要检查一个用户数据库，但是在我们的例子中只有单一的用户因此没有必要。

error_handler 回调函数是用于给客户端发送未授权错误代码。像我们处理其它的错误代码，这里我们定制一个包含 JSON 数据格式而不是 HTML 的响应。

随着认证系统的建立，所剩下的就是把需要认证的函数添加 @auth.login_required 装饰器。例如:

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})
如果现在要尝试使用 curl 调用这个函数我们会得到:

$ curl -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 36
WWW-Authenticate: Basic realm="Authentication Required"
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 06:41:14 GMT

{
  "error": "Unauthorized access"
}
为了能够调用这个函数我们必须发送我们的认证凭据:

$ curl -u miguel:python -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 316
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 06:46:45 GMT

{
  "tasks": [
    {
      "title": "Buy groceries",
      "done": false,
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "uri": "http://localhost:5000/todo/api/v1.0/tasks/1"
    },
    {
      "title": "Learn Python",
      "done": false,
      "description": "Need to find a good Python tutorial on the web",
      "uri": "http://localhost:5000/todo/api/v1.0/tasks/2"
    }
  ]
}
认证扩展给予我们很大的自由选择哪些函数需要保护，哪些函数需要公开。

为了确保登录信息的安全应该使用 HTTP 安全服务器(例如: https://...)，这样客户端和服务器之间的通信都是加密的，以防止传输过程中第三方看到认证的凭据。
----------------------------------------------------------------------------------------------------






//蓝图
//blueprint

api.
init_app(app)
Initialize this class with the given flask.Flask application or flask.Blueprint object.

Parameters:	app (flask.Blueprint) – the Flask application or blueprint object
Examples:

api = Api()
api.add_resource(...)
api.init_app(app)











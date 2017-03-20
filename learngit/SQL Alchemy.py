Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB_URI))
session = scoped_session(Session)

Sessionmaker类似于工厂类，实现__call__,实例Session可以：
session = Session(bind = engine),生成session对象
Scope_session可使程序员不用关注线程


class sessionmaker(_SessionClassMethods):
    """A configurable :class:`.Session` factory.

    The :class:`.sessionmaker` factory generates new
    :class:`.Session` objects when called, creating them given
    the configurational arguments established here.

    e.g.::

        # global scope
        Session = sessionmaker(autoflush=False)

        # later, in a local scope, create and use a session:
        sess = Session()

    Any keyword arguments sent to the constructor itself will override the
    "configured" keywords::

        Session = sessionmaker()

        # bind an individual session to a connection
        sess = Session(bind=connection)

    The class also includes a method :meth:`.configure`, which can
    be used to specify additional keyword arguments to the factory, which
    will take effect for subsequent :class:`.Session` objects generated.
    This is usually used to associate one or more :class:`.Engine` objects
    with an existing :class:`.sessionmaker` factory before it is first
    used::

        # application starts
        Session = sessionmaker()

        # ... later
        engine = create_engine('sqlite:///foo.db')
        Session.configure(bind=engine)

        sess = Session()

    .. seealso:

        :ref:`session_getting` - introductory text on creating
        sessions using :class:`.sessionmaker`.

    """

    def __init__(self, bind=None, class_=Session, autoflush=True,
                 autocommit=False,
                 expire_on_commit=True,
                 info=None, **kw):
        """Construct a new :class:`.sessionmaker`.

        All arguments here except for ``class_`` correspond to arguments
        accepted by :class:`.Session` directly.  See the
        :meth:`.Session.__init__` docstring for more details on parameters.

        :param bind: a :class:`.Engine` or other :class:`.Connectable` with
         which newly created :class:`.Session` objects will be associated.
        :param class_: class to use in order to create new :class:`.Session`
         objects.  Defaults to :class:`.Session`.
        :param autoflush: The autoflush setting to use with newly created
         :class:`.Session` objects.
        :param autocommit: The autocommit setting to use with newly created
         :class:`.Session` objects.
        :param expire_on_commit=True: the expire_on_commit setting to use
         with newly created :class:`.Session` objects.
        :param info: optional dictionary of information that will be available
         via :attr:`.Session.info`.  Note this dictionary is *updated*, not
         replaced, when the ``info`` parameter is specified to the specific
         :class:`.Session` construction operation.

         .. versionadded:: 0.9.0

        :param \**kw: all other keyword arguments are passed to the
         constructor of newly created :class:`.Session` objects.

        """
        kw['bind'] = bind
        kw['autoflush'] = autoflush
        kw['autocommit'] = autocommit
        kw['expire_on_commit'] = expire_on_commit
        if info is not None:
            kw['info'] = info
        self.kw = kw
        # make our own subclass of the given class, so that
        # events can be associated with it specifically.
        self.class_ = type(class_.__name__, (class_,), {})    //sessionmaker的make之处

    def __call__(self, **local_kw):
        """Produce a new :class:`.Session` object using the configuration
        established in this :class:`.sessionmaker`.

        In Python, the ``__call__`` method is invoked on an object when
        it is "called" in the same way as a function::

            Session = sessionmaker()
            session = Session()  # invokes sessionmaker.__call__()

        """
        for k, v in self.kw.items():
            if k == 'info' and 'info' in local_kw:
                d = v.copy()
                d.update(local_kw['info'])
                local_kw['info'] = d
            else:
                local_kw.setdefault(k, v)
        return self.class_(**local_kw)       //Session对象执行类的__call__时，即Session(...)时，返回cl_类实例

    def configure(self, **new_kw):
        """(Re)configure the arguments for this sessionmaker.

        e.g.::

            Session = sessionmaker()

            Session.configure(bind=create_engine('sqlite://'))
        """
        self.kw.update(new_kw)

    def __repr__(self):
        return "%s(class_=%r,%s)" % (
            self.__class__.__name__,
            self.class_.__name__,
            ", ".join("%s=%r" % (k, v) for k, v in self.kw.items())
        )


Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB_URI))
session = scoped_session(Session)



s1 = Session()

print type(Session)

print type(session)

print type(s1)

# <class 'sqlalchemy.orm.session.sessionmaker'>
# <class 'sqlalchemy.orm.scoping.scoped_session'>
# <class 'sqlalchemy.orm.session.Session'>


Defining Attributes

In the previous example, the Column objects are automatically named with the name of the attribute to which they are assigned.

To name columns explicitly with a name distinct from their mapped attribute, just give the column a name. Below, column “some_table_id” is mapped to the “id” attribute of SomeClass, but in SQL
 will be represented as “some_table_id”:

class SomeClass(Base):
    __tablename__ = 'some_table'
    id = Column("some_table_id", Integer, primary_key=True)



//dynamic extention

Attributes may be added to the class after its construction, and they will be added to the underlying Table and mapper() definitions as appropriate:

SomeClass.data = Column('data', Unicode)
SomeClass.related = relationship(RelatedInfo)



Disconnect Handling - Optimistic

The most common approach is to let SQLAlchemy handle disconnects as they occur, at which point the pool is refreshed. This assumes the Pool is used in conjunction with a Engine. The Engine has 
logic which can detect disconnection events and refresh the pool automatically.

When the Connection attempts to use a DBAPI connection, and an exception is raised that corresponds to a “disconnect” event, the connection is invalidated. The Connection then calls the Pool.
recreate() method, effectively invalidating all connections not currently checked out so that they are replaced with new ones upon next checkout:

from sqlalchemy import create_engine, exc
e = create_engine(...)
c = e.connect()

try:
    # suppose the database has been restarted.
    c.execute("SELECT * FROM table")
    c.close()
except exc.DBAPIError, e:
    # an exception is raised, Connection is invalidated.
    if e.connection_invalidated:
        print("Connection was invalidated!")

# after the invalidate event, a new connection
# starts with a new Pool
c = e.connect()
c.execute("SELECT * FROM table")
The above example illustrates that no special intervention is needed, the pool continues normally after a disconnection event is detected. However, an exception is raised. In a typical 
web application using an ORM Session, the above condition would correspond to a single request failing with a 500 error, then the web application continuing normally beyond that. 
Hence the approach is “optimistic” in that frequent database restarts are not anticipated.




Once established, the newly resulting Engine will request a connection from the underlying Pool once Engine.connect() is called, or a method which depends on it such as Engine.execute() is invoked.
 The Pool in turn will establish the first actual DBAPI connection when this request is received. The create_engine() call itself does not establish any actual DBAPI connections directly.


pool_size=5 – the number of connections to keep open inside the connection pool. This used with QueuePool as well as SingletonThreadPool. With QueuePool, a pool_size setting of 0 indicates 
no limit; to disable pooling, set poolclass to NullPool instead.

pool_recycle=-1? – this setting causes the pool to recycle connections after the given number of seconds has passed. It defaults to -1, or no timeout. For example, setting to 3600 means 
connections will be recycled after one hour. Note that MySQL in particular will disconnect automatically if no activity is detected on a connection for eight hours (although this is configurable 
with the MySQLDB connection itself and the server configuration as well).
pool_timeout=30? – number of seconds to wait before giving up on getting a connection from the pool. This is only used with QueuePool.



Pooling

The Engine will ask the connection pool for a connection when the connect() or execute() methods are called. The default connection pool, QueuePool, will open connections to the database on 
an as-needed basis. As concurrent statements are executed, QueuePool will grow its pool of connections to a default size of five, and will allow a default “overflow” of ten. Since the Engine 
is essentially “home base” for the connection pool, it follows that you should keep a single Engine per database established within an application, rather than creating a new one for each 
connection.

The typical usage of create_engine() is once per particular database URL, held globally for the lifetime of a single application process. A single Engine manages many individual DBAPI 
connections on behalf of the process and is intended to be called upon in a concurrent fashion. The Engine is not synonymous to the DBAPI connect function, which represents just one connection 
resource - the Engine is most efficient when created just once at the module level of an application, not per-object or per-function call.





//定制base，或mixin

from sqlalchemy.ext.declarative import declared_attr

class MyMixin(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}
    __mapper_args__= {'always_refresh': True}

    id =  Column(Integer, primary_key=True)

class MyModel(MyMixin, Base):
    name = Column(String(1000))



If the Base did define an attribute of the same name, the class placed first in the inherits list would determine which attribute is used on the newly defined class.

from sqlalchemy.ext.declarative import declared_attr

class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}

    id =  Column(Integer, primary_key=True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(cls=Base)

class MyModel(Base):
    name = Column(String(1000))
Where above, MyModel and all other classes that derive from Base will have a table name derived from the class name, an id primary key column, as well as the “InnoDB” engine for MySQL.
BaseModel = declarative_base()
class User(BaseModel):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }



>>> session.commit()
commit() flushes whatever remaining changes remain to the database, and commits the transaction. The connection resources referenced by the session are now returned to the connection pool. Subsequent operations with this session will occur in a new transaction, which will again re-acquire connection resources when first needed.



//query
It features a generative interface whereby successive calls return a new Query object, a copy of the former with additional criteria and options associated with it.


//数据库迁移，不用删除表，直接加字段#用sql语句可以做到，改model，改table，法2：





default_benchmark = session.query(Benchmark).order_by(Benchmark.checkin_time.desc()).first()


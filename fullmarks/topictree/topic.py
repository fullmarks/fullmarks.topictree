from five import grok
from plone.directives import form
from plone.dexterity import content

from zope import schema

from z3c.form import group, field
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from fullmarks.topictree import MessageFactory as _


# Interface class; used to define content-type schema.

class ITopic(form.Schema):
    """
    Topic for a Topic Tree
    """
    


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Topic(content.Container):
    grok.implements(ITopic)
    
    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# topic_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    grok.context(ITopic)
    grok.require('zope2.View')
    
    # grok.name('view')

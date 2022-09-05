from xmlrpc.client import DateTime


class Article:
  Title = ""
  Date = DateTime()
  Content = ""

  def __init__(self, title, date, content):
    self.Title = title
    self.Date = date
    self.Content = content
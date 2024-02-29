import collections

class SalesItem:
  def __init__(self, branch, totalSales, date):
    self.branch = branch
    self.totalSales = totalSales
    self.date = date

# <summary >
# It has been a busy year at mountain warehouse, having made lots of sales.
# Management would like to know which branch made the most in revenue.
# For this challenge you will be given an array of sales broken down by Branch and Date.
# You will need to sum all branch across multiple days and identify which branch had the highest sales overall
# Assume that there is only one branch with the highest total
# We have provided some starting code but if you know of a better method then go ahead with that
# </summary >
# <param name = "sales" > The array of sales items < /param >
# <returns > The branch with the best performing sales < /returns >


def CalculateBestBranch(sales):

  branchSales = {}

  for item in sales:
    if item.branch in branchSales.keys():
      value = branchSales[item.branch] + item.totalSales
      branchSales[item.branch] = value 
    else:
      branchSales[item.branch] = item.totalSales
      
  sortedDict = dict(sorted(branchSales.items(), key=lambda kv:kv[1], reverse=True))

  branch = ""

  for key in sortedDict.keys():
    branch = key
    break

  return branch

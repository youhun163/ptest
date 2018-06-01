from  pyecharts import Bar
bar =  Bar(" tubiao 1")
bar.add("cloth",["shou","shangyi","kuzi"],[10,20,30],is_more_utils=True)
bar.render()

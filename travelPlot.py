# Author:  Andy Ngo
# Course:  CSCE 101
# Assignment:  5 – Travel Management System, Plotting
# Date:  4/15/2018

from travelClass import travelItem
import numpy as np
import matplotlib.pyplot as plt


def plotTravel(itemRecords):
    '''
        NOTE: - sorted(...) sometimes does not correctly sort the items based on itemId.
                Feel free to try to trouble shoot that yourself if you want.
              - Colors aren't exactly the same as in the assignment pdf.
              - Didn't mess with making the overall figure bigger to accomodate for
                the figure number and caption. 
              - The available end value for Italy is 85 here instead of 75. I'm not
                sure if it's supposed to be that way or not. But, based on the data
                you have in the csv's, it makes sense.
              - I accounted for the 3 edge cases you texted me about.
                  - If available start < 0 for a travel item, I just don't read it in.
                    You can see that in readItems(...).
                  - If available end < 0, the program exits. You can see that in printSummary(...).
                  - If available end < available start, the program exits. You can see that in
                    printSummar(...).
    '''
    sorted(itemRecords.values(), key=lambda travelItem: travelItem.itemID)

    N = len(itemRecords)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35        # the width of the bars

    fig, ax = plt.subplots()

    start_rect = ax.bar(ind, [rec.getAvailableStart() for rec in itemRecords.values()], width, color='red')
    end_rect = ax.bar(ind + width, [rec.getAvailableEnd() for rec in itemRecords.values()], width, color='teal')

    # add some text for labels, title and axes ticks
    ax.set_title('Travel Availability, by tour')
    ax.set_ylabel('Available')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(["{}\nID: {}".format(rec.getName(),rec.getID()) for rec in itemRecords.values()])
    ax.legend(('Start', 'End'))

    fig.text(0.2, 0.005, "Figure 1: Plot of Travel Inventories", ha='center')

    def autolabel(rects):
        """ Attach a text label above each bar displaying its height """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., height,
                    '%d' % int(height),
                    ha='center', va='bottom')

    autolabel(start_rect)
    autolabel(end_rect)

    plt.show()
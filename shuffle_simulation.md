# Shuffle Simulation

After the map step I had three files in map_outputs, one for each partition. Each one just had a bunch of (category, 1) pairs, but the categories were still split up between the files. Like partition1 had 7 laptops, partition2 had 7, and partition3 had 6.

For the shuffle I wrote shuffle_step.py. It reads all three map files and puts every 1 into a list under its category using a dictionary. Then it saves that to shuffle_outputs/grouped.json.

This is what I got:

    laptop:    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    camera:    [1,1,1,1,1,1,1,1,1,1,1,1,1]
    projector: [1,1,1,1,1,1,1]

On my laptop this was easy because all the files were in one folder. In a real system each partition would be on a different computer, so the shuffle would have to send all the laptop values to one machine and all the camera values to another. That's why the shuffle is the slow part, since all that data has to go over the network.
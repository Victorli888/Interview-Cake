using System;
using System.Collections.Generic;
using System.Linq;

public static List<Meeting> MergeRanges(List<Meeting> meetings)
{
// Make a copy so we don't destroy the input, and sort by start time
var sortedMeetings = meetings.Select(m => new Meeting(m.StartTime, m.EndTime))
    .OrderBy(m => m.StartTime).ToList();

// Initialize mergedMeetings with the earliest meeting
var mergedMeetings = new List<Meeting> { sortedMeetings[0] };

    foreach (var currentMeeting in sortedMeetings)
{
    var lastMergedMeeting = mergedMeetings.Last();

    if (currentMeeting.StartTime <= lastMergedMeeting.EndTime)
    {
        // If the current meeting overlaps with the last merged meeting, use the
        // later end time of the two
        lastMergedMeeting.EndTime =
            Math.Max(lastMergedMeeting.EndTime, currentMeeting.EndTime);
    }
    else
    {
        // Add the current meeting since it doesn't overlap
        mergedMeetings.Add(currentMeeting);
    }
}

return mergedMeetings;
}

package Programmers.Java;

import java.util.*;

class Solution {
    public String[] solution(String[][] plans) {
        List<String> answer = new ArrayList<>();
        Deque<Plan> stack = new ArrayDeque<>();

        Arrays.sort(plans, (a, b) -> a[1].compareTo(b[1]));


        for (int i = 0; i < plans.length; i++) {
            String[] p = plans[i];
            Plan plan = new Plan(p[0],p[1],p[2]);

            if (!stack.isEmpty()) {
                Plan prevPlan = stack.pop();
                int timeLeft = plan.getStartTime() - prevPlan.getStartTime();
                if (prevPlan.getDuration() > timeLeft) {
                    prevPlan.setDuration(prevPlan.getDuration() - timeLeft);
                    stack.push(prevPlan);
                }
                else {
                    answer.add(prevPlan.getName());
                    timeLeft -= prevPlan.getDuration();
                    while (!stack.isEmpty()) {
                        Plan stoppedPlan = stack.pop();
                        if (timeLeft < stoppedPlan.getDuration()) {
                            stoppedPlan.setDuration(stoppedPlan.getDuration() - timeLeft);
                            stack.push(stoppedPlan);
                            break;
                        } else {
                            answer.add(stoppedPlan.getName());
                            timeLeft -= stoppedPlan.getDuration();
                        }
                    }
                }

            }
            stack.push(plan);

        }

        while (!stack.isEmpty()) {
            answer.add(stack.pop().getName());
        }

        return answer.toArray(String[]::new);
    }

    static class Plan {
        private String name;
        private int startTime;
        private int duration;

        public Plan(String name, String startTime, String duration) {
            this.name = name;
            this.startTime = timeToMinute(startTime);
            this.duration = Integer.parseInt(duration);
        }

        private int timeToMinute(String startTime) {
            String[] hm = startTime.split(":");
            return 60 * Integer.parseInt(hm[0]) + Integer.parseInt(hm[1]);
        }

        public String getName() {
            return this.name;
        }
        public int getStartTime() {
            return this.startTime;
        }
        public int getDuration() {
            return this.duration;
        }

        public void setDuration(int duration) {
            this.duration = duration;
        }

    }

}

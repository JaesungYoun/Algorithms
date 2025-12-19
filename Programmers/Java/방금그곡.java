package Programmers.Java;
import java.util.*;

public class 방금그곡 {

    class Solution {
        public String solution(String m, String[] musicinfos) {
            List<String[]> answerList = new ArrayList<>();

            for (String mi : musicinfos) {
                String[] info = mi.split(",");
                int start = to_minute(info[0]);
                int end = to_minute(info[1]);
                String title = info[2];
                String music = info[3];

                int play_time = end - start;

                String melody = change(music);
                m = change(m);

                StringBuilder fullMelody = new StringBuilder();

                int repeat = play_time / melody.length();
                int remain = play_time % melody.length();

                for (int i = 0; i < repeat; i++) {
                    fullMelody.append(melody);
                }

                fullMelody.append(melody.substring(0, remain));


                if (fullMelody.toString().contains(m)) {
                    answerList.add(new String[] {title, String.valueOf(play_time)});
                }

                answerList.sort((a,b) -> Integer.compare(Integer.parseInt(b[1]), Integer.parseInt(a[1])));

            }

            if (!answerList.isEmpty()) {
                return answerList.get(0)[0];
            } else {
                return "(None)";
            }

        }

        private String change(String music) {
            if (music.contains("A#")) {
                music = music.replace("A#", "a");
            }
            if (music.contains("F#")) {
                music = music.replace("F#", "f");
            }
            if (music.contains("B#")) {
                music = music.replace("B#", "b");
            }
            if (music.contains("C#")) {
                music = music.replace("C#", "c");
            }
            if (music.contains("G#")) {
                music = music.replace("G#", "g");
            }
            if (music.contains("D#")) {
                music = music.replace("D#", "d");
            }
            return music;
        }

        private int to_minute(String time) {
            String[] hm = time.split(":");
            return Integer.parseInt(hm[0]) * 60 + Integer.parseInt(hm[1]);
        }
    }
}

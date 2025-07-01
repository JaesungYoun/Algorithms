package Programmers.Java;

import java.util.*;

class 무인도여행 {
    public int[] solution(String[] maps) {
        int n = maps.length;
        int m = maps[0].length();
        List<Integer> answer = new ArrayList<>();
        int[][] visited = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maps[i].charAt(j) != 'X' && visited[i][j] == 0) {
                    int day = bfs(maps, i, j, visited, n, m);
                    answer.add(day);
                }
            }
        }

        if (answer.isEmpty()) return new int[] {-1};

        Collections.sort(answer);
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};

    public int bfs(String[] maps, int x, int y, int[][] visited, int n, int m) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {x, y});
        visited[x][y] = 1;

        int day = Integer.parseInt(String.valueOf(maps[x].charAt(y)));

        while (!queue.isEmpty()) {
            int[] point = queue.poll();
            int cx = point[0];
            int cy = point[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m &&
                        visited[nx][ny] == 0 && maps[nx].charAt(ny) != 'X') {

                    queue.offer(new int[] {nx, ny});
                    visited[nx][ny] = 1;
                    day += Integer.parseInt(String.valueOf(maps[nx].charAt(ny)));
                }
            }
        }

        return day;
    }
}


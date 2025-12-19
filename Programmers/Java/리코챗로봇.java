package Programmers.Java;


import java.util.*;

public class 리코챗로봇 {

    class Solution {

        static int[] dx = {-1, 1, 0, 0};
        static int[] dy = {0, 0, -1, 1};

        public int solution(String[] board) {
            int answer = -1;

            int n = board.length;
            int m = board[0].length();

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (board[i].charAt(j) == 'R') {
                        answer = bfs(i, j, board);
                    }
                }
            }

            return answer;
        }

        public int bfs(int x, int y, String[] board) {
            int n = board.length;
            int m = board[0].length();

            int[][] visited = new int[n][m];
            Queue<int[]> q = new ArrayDeque<>();
            q.offer(new int[]{x, y});
            visited[x][y] = 1;

            while (!q.isEmpty()) {
                int[] cur = q.poll();
                int cx = cur[0];
                int cy = cur[1];

                for (int dir = 0; dir < 4; dir++) {
                    int nx = cx;
                    int ny = cy;

                    while (nx >= 0 && nx < n && ny >=0 && ny < m || board[nx].charAt(ny) != 'D') {
                        int tx = nx + dx[dir];
                        int ty = ny + dy[dir];

                        if (tx < 0 || tx >= n || ty < 0 || ty >= m || board[tx].charAt(ty) == 'D') break;

                        nx = tx;
                        ny = ty;
                    }

                    if (visited[nx][ny] > 0) continue;

                    visited[nx][ny] = visited[cx][cy] + 1;

                    if (board[nx].charAt(ny) == 'G') {
                        return visited[nx][ny] - 1;
                    }

                    q.offer(new int[]{nx, ny});
                }
            }

            return -1;
        }
    }

}

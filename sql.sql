WITH anon_3 AS NOT MATERIALIZED (
  SELECT 
    json_group_array(
      json_object('primary_key', anon_4.id)
    ) AS obj, 
    todo.id AS id,
    anon_4.id as user_id
  FROM 
    (
      SELECT 
        user.id AS id 
      FROM 
        user
    ) AS anon_4 
    JOIN todo_user ON todo_user.user_id = anon_4.id 
    JOIN todo ON todo.id = todo_user.todo_id 
  GROUP BY 
    todo.id
) 
SELECT 
  '[' || coalesce(
    group_concat(anon_2.sql_rest), 
    ''
  ) || ']' AS anon_1 
FROM 
  (
    SELECT 
      json_object(
        'primary_key', 
        todo.id, 
        'instruction', 
        todo.comment, 
        'creation_time', 
        todo.created_at, 
        'preference', 
        todo.priority, 
        'is_principal', 
        todo.is_main, 
        'worker', 
        todo.worker_fullname, 
        'deadline', 
        todo.due_date, 
        'amount', 
        todo.count, 
        'users', 
        CASE WHEN (anon_3.id IS NOT NULL) THEN json(anon_3.obj) ELSE json('[]') END
      ) AS sql_rest, 
      todo.id AS id 
    FROM 
      todo 
      LEFT OUTER JOIN anon_3 ON todo.id = anon_3.id 
    GROUP BY 
      todo.id 
    ORDER BY 
      anon_3.user_id DESC 
    LIMIT 
      20 OFFSET 0
  ) AS anon_2

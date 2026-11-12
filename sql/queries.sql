-- Parte 4: Exercícios com SQL (abrir o db.sqlite3 no DB Browser ou na extensão SQLite do VSCode)
-- Tabelas criadas pelo Django: blog_post, blog_comment, blog_category,
-- blog_post_categories (tabela intermediária post x categoria) e auth_user.

-- 1) Todos os posts, ordenados pela data, sendo o mais recente primeiro
SELECT *
FROM blog_post
ORDER BY date DESC;

-- 2) Para um post com comentários (post id = 1), todos os seus comentários
SELECT *
FROM blog_comment
WHERE post_id = 1;

-- 3) Para um post com comentários (post id = 1), todos os seus comentários com
--    todas as colunas de comentário (exceto post_id), o título do post e a sua
--    data de publicação renomeada para post_date
SELECT c.id,
       c.text,
       c.date,
       c.author_id,
       p.title,
       p.date AS post_date
FROM blog_comment AS c
JOIN blog_post AS p ON p.id = c.post_id
WHERE c.post_id = 1;

-- 4) Para uma categoria (categoria id = 1), todos os posts pertencentes a ela,
--    incluindo as colunas da tabela de categoria e da tabela de posts
SELECT cat.*,
       p.*
FROM blog_category AS cat
JOIN blog_post_categories AS pc ON pc.category_id = cat.id
JOIN blog_post AS p ON p.id = pc.post_id
WHERE cat.id = 1;

-- 5) Todas as categorias que possuem dois ou mais posts
SELECT cat.*,
       COUNT(pc.post_id) AS total_posts
FROM blog_category AS cat
JOIN blog_post_categories AS pc ON pc.category_id = cat.id
GROUP BY cat.id
HAVING COUNT(pc.post_id) >= 2;

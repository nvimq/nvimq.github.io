script = """(() => {
  const badges = [];
  const seen = new Set();

  document.querySelectorAll('img').forEach(img => {
    if (!img.src.includes('badge') && !img.src.includes('avatar') && !img.src.includes('certificate') && !img.src.includes('mascot')) return;

    let fiberKey = Object.keys(img).find(k => k.startsWith('__reactFiber$'));
    if (!fiberKey) return;

    let curr = img[fiberKey];
    let detailId = null;
    let fallbackTitle = img.alt || "";

    const imgMatch = img.src.match(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/i);
    const ignoreId = imgMatch ? imgMatch[0].toLowerCase() : null;

    function searchForId(obj) {
       if (!obj || typeof obj !== 'object') return null;
       
       // Ищем конкретные ключи, которые отвечают за ID награды
       const possibleKeys = ['id', 'rewardId', 'userRewardId', 'detailId', 'uuid'];
       for (const key of possibleKeys) {
          if (typeof obj[key] === 'string') {
             const m = obj[key].match(/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i);
             if (m && m[0].toLowerCase() !== ignoreId) return m[0];
          }
       }
       
       if (obj.href && typeof obj.href === 'string') {
          const m = obj.href.match(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/i);
          if (m && m[0].toLowerCase() !== ignoreId) return m[0];
       }

       // Ищем внутри вложенных объектов, где обычно лежат данные
       const nested = ['item', 'badge', 'reward', 'data', 'row'];
       for (const key of nested) {
          if (obj[key]) {
             const res = searchForId(obj[key]);
             if (res) return res;
          }
       }
       return null;
    }

    while (curr) {
      if (curr.memoizedProps) {
        detailId = searchForId(curr.memoizedProps);
        
        if (!fallbackTitle && curr.memoizedProps.title && typeof curr.memoizedProps.title === 'string') {
           fallbackTitle = curr.memoizedProps.title;
        }
      }
      if (detailId) break;
      curr = curr.return;
    }

    if (detailId) {
      const url = "https://app.letsdefend.io/my-rewards/detail/" + detailId;
      if (!seen.has(url)) {
        seen.add(url);
        badges.push({
          title: fallbackTitle.trim() || "LetsDefend Badge",
          url: url,
          img: img.src
        });
      }
    }
  });

  copy(JSON.stringify(badges, null, 2));
  console.log("✅ УСПЕШНО! Найдено бейджей:", badges.length);
})();"""
print("Script ready to send to user.")
